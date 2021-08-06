import logging

from fastapi import APIRouter, Depends, HTTPException

from city_details.api.api_v1.routes.all_request_router import CityDetailsRoute
from city_details.core.interfaces import ICityDetails
from city_details.crud.city import get_city
from city_details.db.mongodb import AsyncIOMotorClient, get_database
from city_details.db.mongodb_utils import get_server_info
from city_details.models.city import ListOfCitiesResponse

__author__ = "Rohit Warke"
__date_created__ = "2021-08-05"
__purpose__ = "This is the City Router that gets the city details"

logger = logging.getLogger(__name__)


class CityRouter(ICityDetails):
    router = APIRouter(route_class=CityDetailsRoute)

    @staticmethod
    @router.get("/cities", response_model=ListOfCitiesResponse, name="cities")
    async def retrieve_cities(city: str, db: AsyncIOMotorClient = Depends(get_database)) -> dict:
        """Cities route to get a list of city names start with input substring
        
        Args:
            city (str): Input string to seach
            db (AsyncIOMotorClient, optional): Database connection.

        Returns:
            Dict: Dictionary containing list of Cities and total count
        """
        try:
            cities = await get_city(conn=db, input_string=city)
            logger.debug(f'FOUND [{len(cities)}] city records')
            cities = ListOfCitiesResponse(cities=cities, count=len(cities))
            return cities
        except Exception as e:
            logger.exception(e)
            raise HTTPException(status_code=500, detail=f"Exception: {e}")

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
