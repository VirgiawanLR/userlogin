from flask import Flask
from flask_restful import Resource, Api, reqparse
from master_resources.signup import SignUp
from master_resources.signin import SignIn
from master_resources.getdata import GetData

app = Flask(__name__)
api = Api(app)



api.add_resource(SignUp, '/signup')
api.add_resource(SignIn, '/signin')
api.add_resource(GetData, '/userdata')

if __name__ == '__main__':
    app.run(debug=True)

