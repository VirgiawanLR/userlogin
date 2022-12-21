from flask_restful import Resource, reqparse
from logic.get_barang import getdata

class GetBarang(Resource):
    def get(self):
        regist_parser = reqparse.RequestParser()
        regist_parser.add_argument('personid', type=int)
        regist_arg = regist_parser.parse_args()
        print(regist_arg)
        data_barang = getdata(regist_arg)

        return data_barang, 200
