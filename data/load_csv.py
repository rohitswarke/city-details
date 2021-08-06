import csv
import os
from typing import TypedDict

from pymongo import MongoClient

__author__ = "Rohit Warke"
__date_created__ = "2021-08-05"
__purpose__ = """This script is to load worldcities.csv file into MongoDB
                 This is a one time script, once the data is loaded in
                 MongoDB, we don't need to run it again."""


def transform(dict_, typed_dict) -> dict:
    """ Convert values in given dictionary to corresponding types in TypedDict . """
    fields = typed_dict.__annotations__
    try:
        data = {name: fields[name](value) for name, value in dict_.items()}
    except ValueError as ve:
        print(f'Go ValueError for {dict_.items()}\n{ve}')
        data = dict()
        for key, value in dict_.items():
            try:
                data[key] = fields[key](value)
            except ValueError:
                # The data is maintained by a community and sometimes the data types are mismatching
                # Handle string -> float -> int type conversion
                print(f'value: {value} | type(value): {type(value)}')
                if len(value) > 0:
                    print(f'Float population found: {value}')
                    data[key] = int(float(value))
                else:
                    data[key] = None
        print(f'modified data: {data}')
    return data


class CSVRecordTypes(TypedDict):
    """ Define the fields and their types in a record.
        Field names must match column names in CSV file header.
    """
    # Sample looks like this:
    # "city","city_ascii","lat","lng","country","iso2","iso3","admin_name","capital","population","id"
    # "Tokyo","Tokyo","35.6897","139.6922","Japan","JP","JPN","Tōkyō","primary","37977000","1392685764"
    city: str
    city_ascii: str
    lat: float
    lng: float
    country: str
    iso2: str
    iso3: str
    admin_name: str
    capital: str
    population: int
    id: int


filename = 'worldcities.csv'
if os.path.exists(filename):
    MONGODB_URL = os.getenv("MONGODB_URL", "")
    mongo_client = MongoClient(
        'mongodb+srv://test-user:test-password@mflix.m2bsj.mongodb.net/CITY_DETAILS?retryWrites=true&w=majority')
    db = mongo_client['CITY_DETAILS']
    collection = db["CITIES"]

    try:
        with open(filename, newline='', encoding="utf8") as file:
            for i, row in enumerate(csv.DictReader(file), 1):
                row = transform(row, CSVRecordTypes)
                # print(f'row {i}: {row}')
                if row:
                    collection.insert_one(row)
    except Exception as e:
        print(f'Exception occurred: {e}')
        raise e
