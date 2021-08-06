import datetime
import logging

from fastapi import APIRouter, HTTPException

from city_details.api.api_v1.routes.all_request_router import CityDetailsRoute
from city_details.core.config import database_name, cities_collection_name
from city_details.core.interfaces import ICityDetails
from city_details.models.health import HealthResponse

__author__ = "Rohit Warke"
__date_created__ = "2021-08-06"
__purpose__ = "This is the health checker router that gets the config and router status."

router = APIRouter(route_class=CityDetailsRoute)
logger = logging.getLogger(__name__)


@router.get("/health", response_model=HealthResponse, name="health:maintenance")
async def health():
    router_status = {}
    try:
        info = []
        is_healthy = True
        configs = [{'database_name': database_name,
                    'cities_collection_name': cities_collection_name}]

        # get the routers that inherit from ICityDetails
        router_status_instances = {}
        for cls in ICityDetails.__subclasses__():
            router_status_instances[cls.__name__] = cls

        for router_name, instance in router_status_instances.items():
            try:
                # execute their get_status() function
                router_status[router_name] = await instance.get_status()
            except Exception as e:
                router_status[router_name] = f'{e}'
                is_healthy = False
                info.append(router_name)

        if is_healthy:
            information = 'All routers are up and running'
        else:
            information = f'Service encountered issue with: [{",".join(info)}]'

        return HealthResponse(
            is_healthy=is_healthy,
            information=information,
            checked_at=datetime.datetime.utcnow().strftime('%Y%m%d %H:%M:%S'),
            configurations=configs,
            router_status=router_status
        )
    except Exception as e:
        logger.exception(f'Exception occurred: {e}')
        status = ''.join([k + '=' + v for k, v in router_status.items()])
        raise HTTPException(status_code=404, detail="UNHEALTHY. " + status)
