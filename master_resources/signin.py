from flask_restful import Resource, reqparse
from master_resources.signup import database

class SignIn(Resource):
    def get(self):
        global database

        signin_parser = reqparse.RequestParser()
        signin_parser.add_argument('username', type=str)
        signin_parser.add_argument('password', type=str)
        signin_data = signin_parser.parse_args()

        USERNAME = signin_data['username']
        PASSWORD = signin_data['password']
        is_Valid = False

        for item in database:
            if (item['username'] == USERNAME and item['password'] == PASSWORD):
                is_Valid = True
        
        if is_Valid:
            return {'messages': 'you"re logged in'}, 200
        else:
            return {'messages': 'username and password not match'}, 400
