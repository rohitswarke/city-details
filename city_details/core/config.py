import logging
import os

from databases import DatabaseURL
from dotenv import load_dotenv
from starlette.datastructures import CommaSeparatedStrings, Secret

from city_details.__version__ import name, __version__

logger = logging.getLogger(__name__)

API_V1_STR = ""

load_dotenv(".env")

MAX_CONNECTIONS_COUNT = int(os.getenv("MAX_CONNECTIONS_COUNT", 10))
MIN_CONNECTIONS_COUNT = int(os.getenv("MIN_CONNECTIONS_COUNT", 10))
SECRET_KEY = Secret(os.getenv("SECRET_KEY", "secret key for project"))

PROJECT_NAME = os.getenv("PROJECT_NAME", name)
VERSION = __version__
DEBUG = True
PRE_LOAD = True
ALLOWED_HOSTS = CommaSeparatedStrings(os.getenv("ALLOWED_HOSTS", ""))

MONGO_DB = os.getenv("MONGO_DB", "CITY_DETAILS")
MONGODB_URL = os.getenv("MONGODB_URL", "")  # deploying without docker-compose

if not MONGODB_URL:
    MONGO_HOST = os.getenv("MONGO_HOST", "localhost")
    MONGO_PORT = int(os.getenv("MONGO_PORT", 27017))
    MONGO_USER = os.getenv("MONGO_USER", "mongoadmin")
    MONGO_PASS = os.getenv("MONGO_PASSWORD", "mongoadmin")
    MONGO_DB = os.getenv("MONGO_DB", "CITY_DETAILS")

    MONGODB_URL = DatabaseURL(
        f"mongodb://{MONGO_USER}:{MONGO_PASS}@{MONGO_HOST}:{MONGO_PORT}/{MONGO_DB}"
    )
else:
    MONGODB_URL = DatabaseURL(MONGODB_URL)

database_name = MONGO_DB
cities_collection_name = "CITIES"
