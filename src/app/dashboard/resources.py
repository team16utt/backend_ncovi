from flask_restful import Resource
from typing import List
from db import *
from bson.json_util import dumps, loads

class ConDeaths(Resource):
    """
    GET REQUEST to get all ConDeaths
    """
    
    def get(self):
        data = find_all('countriesDeath',{}, disable_field={"_id":0})
        return {"data": list(data),
                "status": "success",
                }, 200