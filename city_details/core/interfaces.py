from abc import ABCMeta
from abc import abstractmethod

__author__ = "Rohit Warke"
__date_created__ = "2021-08-05"
__purpose__ = "This is where we store the interfaces"


class ICityDetails:
    """This is the interface for the routers
    """
    __metaclass__ = ABCMeta

    @staticmethod
    @abstractmethod
    async def get_status(self):
        """Executed by the health checker to get the status of the router
        """
        raise NotImplementedError('get_status is not implemented')
