from typing import Optional, List

# from bson import ObjectId
from pydantic import BaseModel

__author__ = "Rohit Warke"
__date_created__ = "2021-08-06"
__purpose__ = "City response"


class CityBase(BaseModel):
    city: str
    city_ascii: Optional[str]
    lat: Optional[float]
    lng: Optional[float]
    country: Optional[str]
    iso2: Optional[str]
    iso3: Optional[str]
    admin_name: Optional[str]
    capital: Optional[str]
    population: Optional[int]
    id: Optional[int]


class CityInDB(CityBase):
    _id: str
    pass


class ListOfCitiesResponse(BaseModel):
    count: int
    cities: List[CityBase] = []
