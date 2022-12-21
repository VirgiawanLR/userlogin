from flask_restful import Resource, reqparse
from logic.alter_sertif import alter_sertif

class PutSertif(Resource):
    def put(self):
        regist_parser = reqparse.RequestParser()
        regist_parser.add_argument('barangid', type=int)
        regist_parser.add_argument('sertifikatid', type=int)
        
        regist_arg = regist_parser.parse_args()
        
        isSaving = alter_sertif(regist_arg)

        if isSaving:
            return {
                "messages": "your goods certification successfully saved"
            }, 200
        else:
            return {
                "message": "bad request"
            }
