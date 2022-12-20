from flask_restful import Resource, reqparse
from logic.getall import *

class GetData(Resource):
    def get(self):
        return getalldata(), 200
