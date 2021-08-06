import json
import logging
from typing import List

from city_details.core.config import database_name, cities_collection_name
from city_details.core.enhanced_json_encoder import EnhancedEncoder
from city_details.db.mongodb import AsyncIOMotorClient
from city_details.models.city import CityInDB

logger = logging.getLogger(__name__)


async def get_city(conn: AsyncIOMotorClient, input_string: str) -> CityInDB:
    cities: List[CityInDB] = []
    # apply regex to check city names starting with input_string
    query = {
        "city": {
            "$regex": '^' + input_string + '.*',
            "$options": 'i'  # case-insensitive
        }
    }
    cursor = conn[database_name][cities_collection_name].find(query)
    async for document in cursor:
        data = json.dumps(document, cls=EnhancedEncoder)
        # logger.debug(f'CITY DATA:\n{data}\n')
        document = json.loads(data)
        cities.append(CityInDB(**document))
    return cities
