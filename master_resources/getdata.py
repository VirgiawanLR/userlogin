from flask_restful import Resource, reqparse
from master_resources.signup import database

class GetData(Resource):
    def get(self):
        getdata_parser = reqparse.RequestParser()
        getdata_parser.add_argument('get', type=str)
        getdata_arg = getdata_parser.parse_args()

        is_OK = getdata_arg['get'] == 'userdata'

        if is_OK:
            return {"database":database}, 200
        else:
            return {"messages": "bad request"}, 400