import logging

from motor.motor_asyncio import AsyncIOMotorClient

from city_details.core.config import MONGODB_URL, MAX_CONNECTIONS_COUNT, MIN_CONNECTIONS_COUNT
from city_details.db.mongodb import db

logger = logging.getLogger(__name__)


async def connect_to_mongo():
    logger.info(f'Connecting to MongoDB...')
    db.client = AsyncIOMotorClient(str(MONGODB_URL),
                                   maxPoolSize=MAX_CONNECTIONS_COUNT,
                                   minPoolSize=MIN_CONNECTIONS_COUNT)
    logger.info("Successfully connected to the database")


async def close_mongo_connection():
    logger.info("Closing database connection...")
    db.client.close()
    logger.info("Connection closed successfully")


async def get_server_info():
    db.client = AsyncIOMotorClient(str(MONGODB_URL),
                                   maxPoolSize=MAX_CONNECTIONS_COUNT,
                                   minPoolSize=MIN_CONNECTIONS_COUNT)
    data = await db.client.server_info()
    return data
