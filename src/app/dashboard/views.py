from flask import Blueprint
from flask_restful import Api
import dashboard.resources as resources


blueprint = Blueprint('dashboard', __name__)

api = Api(blueprint)
api.add_resource(resources.ConDeaths,'/countries_death')