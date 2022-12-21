from flask_restful import Resource
from logic.get_allbarang import getalldata

class GetAllBarang(Resource):
    def get(self):
        return getalldata(), 200
