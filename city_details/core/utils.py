import argparse
import json
import logging

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from starlette.responses import JSONResponse

from city_details.core.enhanced_json_encoder import EnhancedEncoder

__author__ = "Rohit Warke"
__date_created__ = "2021-08-05"
__purpose__ = "This is the utilities file where we keep the helper functions"

logger = logging.getLogger(__name__)


def create_aliased_response(model: BaseModel) -> JSONResponse:
    return JSONResponse(content=jsonable_encoder(model, by_alias=True))


def str2bool(v):
    """String to boolean

    Args:
        v (string): String
    """
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False


def get_command_line_arguments():
    """Getting command prompt line arguments
    """
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description="Program to start city details user interface"
    )
    parser.add_argument(
        '-s',
        '--server',
        dest='host_address',
        help='Provide Host Address',
        default='0.0.0.0'
    )
    parser.add_argument(
        '-p',
        '--port',
        dest='port_number',
        help='Provide Port Number',
        default=8086
    )
    args = parser.parse_args()
    host = args.host_address
    port = args.port_number
    return host, port


def convert_to_dict(data) -> dict:
    """Function to apply enhance encoding and return dictionary object

    Args:
        data (json): Input json data to encode

    Returns:
        dict: Encoded dictionary
    """
    try:
        data = json.dumps(data, cls=EnhancedEncoder)
        return json.loads(data)
    except Exception as e:
        logger.exception(f'Exception while converting data to dict: {e}')
        raise e
