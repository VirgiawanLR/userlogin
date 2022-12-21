from flask import Flask
from flask_restful import Resource, Api, reqparse
from master_resources.signup import SignUp
from master_resources.signin import SignIn
from master_resources.getdata import GetData
from master_resources.postbarang import RegistBarang
from master_resources.getownbarang import GetBarang
from master_resources.getallbarang import GetAllBarang
from master_resources.postsertif import RegistSertif
from master_resources.putsertif import PutSertif
from master_resources.cekbarang import CekBarang

app = Flask(__name__)
api = Api(app)



api.add_resource(SignUp, '/signup')
api.add_resource(SignIn, '/signin')
api.add_resource(GetData, '/userdata')
api.add_resource(RegistBarang, '/registbarang')
api.add_resource(GetBarang, '/getbarangsendiri')
api.add_resource(GetAllBarang, '/getbarangall')
api.add_resource(RegistSertif, '/regisertif')
api.add_resource(PutSertif, '/putsertif')
api.add_resource(CekBarang, '/cekbarang')

if __name__ == '__main__':
    app.run(debug=True)

