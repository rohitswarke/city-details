from fastapi import APIRouter

from city_details.api.api_v1.routes import health_checker_router, ui_router, city_router

__author__ = "Rohit Warke"
__date_created__ = "2021-08-05"
__purpose__ = "The routers are required to add here. Within each router, we add the routes (endpoints)"

router = APIRouter()
router.include_router(city_router.CityRouter.router, tags=["city-details"])
router.include_router(health_checker_router.router, tags=["maintenance"])
router.include_router(ui_router.UIRouter.router, tags=["ui-portal"])
