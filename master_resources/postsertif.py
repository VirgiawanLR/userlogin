from flask_restful import Resource, reqparse
from logic.savesertif import save_sertif

class RegistSertif(Resource):
    def post(self):
        regist_parser = reqparse.RequestParser()
        regist_parser.add_argument('personid', type=int)
        regist_arg = regist_parser.parse_args()
        
        isSaving = save_sertif(regist_arg)

        if isSaving:
            return {
                "messages": "your goods certification successfully saved"
            }, 200
        else:
            return {
                "message": "bad request"
            }
