from flask_restful import Resource, reqparse
import logic.email_check as email_check


database = []

def save_data(new_data):
    database
    database.append(new_data)
    # try:
    # except:
    #     database = [new_data]

class SignUp(Resource):
    def put(self):

        signup_parser = reqparse.RequestParser()
        signup_parser.add_argument('username', type=str)
        signup_parser.add_argument('password', type=str)
        signup_parser.add_argument('conf_password', type=str)
        signup_parser.add_argument('email', type=str)
        signup_parser.add_argument('fullname', type=str)
        
        self.signup_data = signup_parser.parse_args()

        is_constraint_fulfilled = (len(self.signup_data['username'])>4) and (len(self.signup_data['password'])>4) and (len(self.signup_data['fullname'])>4)
        is_pass_confpass_same = self.signup_data['password'] == self.signup_data['conf_password']
        is_email_valid = email_check.check(self.signup_data['email'])
        all_constraints = is_constraint_fulfilled and is_pass_confpass_same and is_email_valid

        if not is_email_valid:
            return {'messages': 'your email is invalid'}, 400
        elif not is_pass_confpass_same:
            return {'messages': 'your password is not match'}, 400
        elif not is_constraint_fulfilled:
            return {'messages': 'your user / pass / fullname is less than 5 characters'}, 400
        elif all_constraints:
            save_data(self.signup_data)
            print(database)
            return {'messages': 'your data have been successfully recorded'}, 200
        else:
            return {'messages': 'bad requests'}, 400
