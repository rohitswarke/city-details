import logging
from pathlib import Path
import os
import uvicorn
from fastapi import FastAPI
from starlette.exceptions import HTTPException
from starlette.middleware.cors import CORSMiddleware
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY

from city_details.api.api_v1.api import router as api_router
from city_details.core.config import PROJECT_NAME, VERSION, ALLOWED_HOSTS, API_V1_STR, DEBUG, PRE_LOAD
from city_details.core.custom_logging import CustomizeLogger
from city_details.core.errors import http_422_error_handler, http_error_handler
from city_details.core.utils import get_command_line_arguments
from city_details.db.mongodb_utils import connect_to_mongo, close_mongo_connection

__author__ = "Rohit Warke"
__date_created__ = "2021-08-05"
__purpose__ = "This is the main file of City Details API interface. " \
              "It starts the service with the configured routes."

logger = logging.getLogger(__name__)
config_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "core", "logging_config.json")


def get_application() -> FastAPI:
    """
    Gets the application
    :return: Application
    """
    global ALLOWED_HOSTS

    application = FastAPI(title=PROJECT_NAME, debug=DEBUG, version=VERSION)

    # set logger
    logger = CustomizeLogger.make_logger(config_path)
    application.logger = logger

    # add the routes
    application.include_router(api_router, prefix=API_V1_STR)
    if PRE_LOAD:
        logger.info(f'PRE-LOADING THE COMPONENTS')
        # add the startup event handler
        application.add_event_handler("startup", connect_to_mongo)
        application.add_event_handler("shutdown", close_mongo_connection)

        application.add_exception_handler(HTTPException, http_error_handler)
        application.add_exception_handler(HTTP_422_UNPROCESSABLE_ENTITY, http_422_error_handler)

    # add middleware
    if not ALLOWED_HOSTS:
        ALLOWED_HOSTS = ["*"]

    application.add_middleware(
        CORSMiddleware,
        allow_origins=ALLOWED_HOSTS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    logger.info(f'PRE-LOAD COMPLETED')
    return application


app = get_application()


def serve():
    host, port = get_command_line_arguments()
    uvicorn.run("city_details:app", host=host, port=port, debug=True, reload=True, workers=2)
