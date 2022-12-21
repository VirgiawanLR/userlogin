from flask_restful import Resource, reqparse
from logic.savebarang import save_barang

class RegistBarang(Resource):
    def post(self):
        regist_parser = reqparse.RequestParser()
        regist_parser.add_argument('namabarang', type=str)
        regist_parser.add_argument('harga', type=int)
        regist_parser.add_argument('personid', type=int)
        regist_parser.add_argument('sertifikatid', type=int)
        regist_arg = regist_parser.parse_args()
        
        isSaving = save_barang(regist_arg)

        if isSaving:
            return {
                "messages": "your data successfully saved"
            }, 200
        else:
            return {
                "message": "bad request"
            }
