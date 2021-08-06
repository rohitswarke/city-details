import logging
import time
from typing import Callable

from fastapi import Request, Response
from fastapi.routing import APIRoute

logger = logging.getLogger(__name__)

__author__ = "Rohit Warke"
__date_created__ = "2021-08-05"
__purpose__ = "Custom route handler which gets executed for every request that is received. " \
              "It adds the header info and logs the duration."


class CityDetailsRoute(APIRoute):
    def get_route_handler(self) -> Callable:
        """Returns the route handler

        Returns:
            Callable: The route handler
        """
        original_route_handler = super().get_route_handler()

        async def custom_route_handler(request: Request) -> Response:
            """Gets the response and adds the duration & api name

            Args:
                request (Request): The request

            Returns:
                Response: The response
            """
            before = time.time()
            try:
                logger.debug(f'=== Got new request ===')
                # Add any custom code here. This will be checked before serving any request
                # For example: Checking request headers, auth token, client cert etc
                response: Response = await original_route_handler(request)
            except Exception as ex:
                logger.exception(f'Unexpected exception occurred: {ex}')
                raise ex

            duration = time.time() - before
            if response is not None:
                response.headers["X-Response-Time"] = str(duration)
                response.headers["X-Response-Api"] = "CityDetails"
                logger.info(f'Sending Response to [{request.client}]. Duration: [{duration}]')
            return response

        return custom_route_handler
