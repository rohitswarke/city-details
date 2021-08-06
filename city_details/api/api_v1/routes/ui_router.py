import logging
from typing import Optional

from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from city_details.api.api_v1.routes.all_request_router import CityDetailsRoute
from city_details.api.api_v1.routes.city_router import CityRouter
from city_details.core.config import API_V1_STR
from city_details.core.interfaces import ICityDetails
from city_details.db.mongodb import AsyncIOMotorClient, get_database
from city_details.db.mongodb_utils import get_server_info

__author__ = "Rohit Warke"
__date_created__ = "2021-08-06"
__purpose__ = "This is the UI Router that displays the UI page"

logger = logging.getLogger(__name__)
templates = Jinja2Templates(directory="templates")


# templates.env.globals["url_for_query"] = url_for_query

class UIRouter(ICityDetails):
    router = APIRouter(route_class=CityDetailsRoute)

    @staticmethod
    @router.get("/", response_class=HTMLResponse, name="index")
    async def home(request: Request, db: AsyncIOMotorClient = Depends(get_database), city: Optional[str] = ""):
        """UI route to display index page
        
        Args:
            city (str): Input string to seach
            db (AsyncIOMotorClient, optional): Database connection.

        Returns:
            [type]: List of Cities
        """
        if city:
            logger.debug(f'Request came to search for cities starting with: [{city}]')
            data = await CityRouter.retrieve_cities(city=city, db=db)
            return templates.TemplateResponse(
                "index.html",
                {
                    "request": request,
                    "api_version_str": API_V1_STR,
                    "data": data,
                    "searched_keyword": city

                }
            )

        return templates.TemplateResponse(
            "index.html",
            {
                "request": request,
                "api_version_str": API_V1_STR
            }
        )

    @staticmethod
    async def get_status(db: AsyncIOMotorClient = Depends(get_database)):
        """Health check to ensure the route is accessible

        Returns:
            [type]: [description]
        """
        try:
            # server_info = await get_server_info(conn=db)
            server_info = await get_server_info()
            return f'SUCCESS. Database Server Info: {server_info}'
        except Exception as e:
            logger.exception(e)
            raise Exception(f'UNSUCCESSFUL. Failed to connect to the database: {e}')
