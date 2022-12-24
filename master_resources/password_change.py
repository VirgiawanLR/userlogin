from flask_restful import Resource, reqparse
from logic.alter_password import retrieve_data, altering

class PassChange(Resource):
    def put(self):
        signin_parser = reqparse.RequestParser()
        signin_parser.add_argument('username', type=str)
        signin_parser.add_argument('current_password', type=str)
        signin_parser.add_argument('password_change', type=str)
        signin_parser.add_argument('confirm_new_password', type=str)
        signin_data = signin_parser.parse_args()

        USERNAME = signin_data['username']
        CURRENT_PASSWORD = signin_data['current_password']
        PASSWORD_CHANGE = signin_data['password_change']
        CONFIRMED_CHANGE = signin_data['confirm_new_password']

        is_constraint_fulfilled = len(PASSWORD_CHANGE)>4
        if not is_constraint_fulfilled:
            return {'messages': 'your new password is less then 5 characters'}, 400

        if PASSWORD_CHANGE != CONFIRMED_CHANGE:
            return {'messages': 'your new password not match with the confirm one'}, 400

        is_Valid = retrieve_data(USERNAME, CURRENT_PASSWORD)

        if is_Valid:
            result = altering(USERNAME, PASSWORD_CHANGE)
            print(result)
            return {'messages': "you're pass changed"}, 200
        else:
            return {'messages': 'username and password not match'}, 400
