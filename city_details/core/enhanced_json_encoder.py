import json
from datetime import datetime

from bson import ObjectId


class EnhancedEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        elif isinstance(o, bytes):
            return o.decode('UTF-8')
        elif isinstance(o, datetime):
            return o.isoformat()
        else:
            return super().default(o)
