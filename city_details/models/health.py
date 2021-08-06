import socket
from typing import Optional

from pydantic import BaseModel

__author__ = "Rohit Warke"
__date_created__ = "2021-08-06"
__purpose__ = "Health response"


class HealthResponse(BaseModel):
    """Returned for all of the health responses

    Args:
        BaseModel ([type]): [description]
    """
    is_healthy: bool
    hostname: str = socket.gethostname()
    information: str
    checked_at: str
    router_status: dict
    configurations: Optional[list] = []
