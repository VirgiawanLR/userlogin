from flask_restful import Resource, reqparse
from logic.oriorimit import check

class CekBarang(Resource):
    def get(self):
        regist_parser = reqparse.RequestParser()
        regist_parser.add_argument('barangid', type=int)
        
        regist_arg = regist_parser.parse_args()
        
        isSaving = check(regist_arg)

        if isSaving == "Original":
            return {
                "messages": "It's the original goods"
            }
        elif isSaving == "Imitation":
            return {
                "message": "Imitation"
            }
        else:
            return {
                "message": "bad request"
            }
