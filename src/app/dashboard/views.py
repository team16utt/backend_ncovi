from flask import Blueprint
from flask_restful import Api
import dashboard.resources as resources
from flask_restful_swagger import swagger


blueprint = Blueprint('dashboard', __name__)

api = swagger.docs(Api(blueprint), apiVersion="0.1",
                   basePath="https://localhost:8080/dashboard",
                   produces=["application/json", "text/html"],
                   api_spec_url="/api/spec",
                   description="API Dashboard for NCOVI")


api.add_resource(resources.ConDeaths,'/countries_death')
api.add_resource(resources.countriesRecover,'/countries_recover')
api.add_resource(resources.globalCasesToday,'/global_cases_today')
api.add_resource(resources.provinces,'/provinces')
api.add_resource(resources.topTrueNews,'/news')
api.add_resource(resources.totalConfirmed,'/confirmed')
api.add_resource(resources.totalVietNam,'/vietnam')
api.add_resource(resources.trendlineVNCases,'/trendline')
api.add_resource(resources.vnPatientCases,'/patients')








