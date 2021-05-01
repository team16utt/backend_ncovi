from flask_restful import Resource, fields
from typing import List
from db import *
from bson.json_util import dumps, loads
from flask_restful_swagger import swagger


@swagger.model
class response_models:
    resource_fields = {
        "status": fields.String,
        "payload": fields.List
    }
class ConDeaths(Resource):
    """
    GET REQUEST to get all ConDeaths
    """
    @swagger.operation(
        notes="Get all countriesDeath",
        responseClass=response_models.__name__,
        nickname="List countries's Death",
        responseMessages=[
            {
                "code":200,
                "message":"Success",
                "data": "Data Info"
            },
            {
                "code":400,
                "message":"Failed",
                "data": "Null"
            }
        ]
    )
    def get(self):
        data = find_all('countriesDeath',{}, disable_field={"_id":0})
        if data:
            return {"data": list(data),
                    "status": "Success",
                    }, 200
        return {"data": "Data is empty",
                "status": "Failed"}, 400

class countriesRecover(Resource):
    """
    GET REQUEST to get all ConDeaths
    """
    @swagger.operation(
        notes="Handle request list all countries's recover infomation",
        responseClass=response_models.__name__,
        nickname="List countries's Death",
        responseMessages=[
            {
                "code":200,
                "message":"Success",
                "data": "Data Info"
            },
            {
                "code":400,
                "message":"Failed",
                "data": "Null"
            }
        ]
    )
    def get(self):
        data = find_all('countriesRecover',{}, disable_field={"_id":0})
        if data:
            return {"data": list(data),
                    "status": "Success",
                    }, 200
        return {"data": "Data is empty",
                "status": "Failed"}, 400

class globalCasesToday(Resource):
    """
    GET REQUEST to get global Cases today
    """
    @swagger.operation(
        notes="Handle request list all countries's global Cases today",
        responseClass=response_models.__name__,
        nickname="List global Cases today",
        responseMessages=[
            {
                "code":200,
                "message":"Success",
                "data": "Data Info"
            },
            {
                "code":400,
                "message":"Failed",
                "data": "Null"
            }
        ]
    )
    def get(self):
        data = find_all('globalCasesToday',{}, disable_field={"_id":0})
        if data:
            return {"data": list(data),
                    "status": "Success",
                    }, 200
        return {"data": "Data is empty",
                "status": "Failed"}, 400

class provinces(Resource):
    """
    Handle all request about provinces
    """
    @swagger.operation(
        notes="Handle request list all provinces in Viet Nam",
        responseClass=response_models.__name__,
        nickname="List Provinces",
        responseMessages=[
            {
                "code":200,
                "message":"Success",
                "data": "Data Info"
            },
            {
                "code":400,
                "message":"Failed",
                "data": "Null"
            }
        ]
    )
    def get(self):
        data = find_all('provinces',{}, disable_field={"_id":0})
        print(data.count())
        if data:
            return {"data": list(data),
                    "status": "Success",
                    }, 200
        return {"data": "Data is empty",
                "status": "Failed"}, 400

class topTrueNews(Resource):
    """
    Handle all request about news
    """
    @swagger.operation(
        notes="Handle request list all best true new",
        responseClass=response_models.__name__,
        nickname="List News",
        responseMessages=[
            {
                "code":200,
                "message":"Success",
                "data": "Data Info"
            },
            {
                "code":400,
                "message":"Failed",
                "data": "Null"
            }
        ]
    )
    def get(self):
        data = find_all('topTrueNews',{}, disable_field={"_id":0})
        print(data.count())
        if data:
            return {"data": list(data),
                    "status": "Success",
                    }, 200
        return {"data": "Data is empty",
                "status": "Failed"}, 400

class totalConfirmed(Resource):
    """
    Handle all request about total cases confirmed
    """
    @swagger.operation(
        notes="Handle request list all confirmed",
        responseClass=response_models.__name__,
        nickname="List total confirmed",
        responseMessages=[
            {
                "code":200,
                "message":"Success",
                "data": "Data Info"
            },
            {
                "code":400,
                "message":"Failed",
                "data": "Null"
            }
        ]
    )
    def get(self):
        data = find_all('totalConfirmed',{}, disable_field={"_id":0})
        print(data.count())
        if data:
            return {"data": list(data),
                    "status": "Success",
                    }, 200
        return {"data": "Data is empty",
                "status": "Failed"}, 400
        
class totalVietNam(Resource):
    """
    Handle all request about total cases confirmed in Viet nam
    """
    @swagger.operation(
        notes="Handle request list all confirmed in Viet Nam",
        responseClass=response_models.__name__,
        nickname="List total confirmed VN",
        responseMessages=[
            {
                "code":200,
                "message":"Success",
                "data": "Data Info"
            },
            {
                "code":400,
                "message":"Failed",
                "data": "Null"
            }
        ]
    )
    def get(self):
        data = find_all('totalVietNam',{}, disable_field={"_id":0})
        print(data.count())
        if data:
            return {"data": list(data),
                    "status": "Success",
                    }, 200
        return {"data": "Data is empty",
                "status": "Failed"}, 400
        
class trendlineVNCases(Resource):
    """
    Handle all request about trend spread of covid in vietnam
    """
    @swagger.operation(
        notes="Handle request list trend spread",
        responseClass=response_models.__name__,
        nickname="List trend line",
        responseMessages=[
            {
                "code":200,
                "message":"Success",
                "data": "Data Info"
            },
            {
                "code":400,
                "message":"Failed",
                "data": "Null"
            }
        ]
    )
    def get(self):
        data = find_all('trendlineVnCases',{}, disable_field={"_id":0})
        print(data.count())
        if data:
            return {"data": list(data),
                    "status": "Success",
                    }, 200
        return {"data": "Data is empty",
                "status": "Failed"}, 400
        
class vnPatientCases(Resource):
    """
    Handle all request about patient in vietnam
    """
    @swagger.operation(
        notes="Handle request list all patients in vietnam",
        responseClass=response_models.__name__,
        nickname="List patients",
        responseMessages=[
            {
                "code":200,
                "message":"Success",
                "data": "Data Info"
            },
            {
                "code":400,
                "message":"Failed",
                "data": "Null"
            }
        ]
    )
    def get(self):
        data = find_all('vnPatientCases',{}, disable_field={"_id":0})
        print(data.count())
        if data:
            return {"data": list(data),
                    "status": "Success",
                    }, 200
        return {"data": "Data is empty",
                "status": "Failed"}, 400