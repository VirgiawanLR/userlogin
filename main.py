from flask import Flask
from flask_restful import Api
from master_resources.signup import SignUp
from master_resources.signin import SignIn
from master_resources.getdata import GetData
from master_resources.postbarang import RegistBarang
from master_resources.getownbarang import GetBarang
from master_resources.getallbarang import GetAllBarang
from master_resources.postsertif import RegistSertif
from master_resources.putsertif import PutSertif
from master_resources.cekbarang import CekBarang
from master_resources.password_change import PassChange


app = Flask(__name__)
api = Api(app)



api.add_resource(SignUp, '/signup')
api.add_resource(SignIn, '/signin')
api.add_resource(GetData, '/getalluserdata')
api.add_resource(RegistBarang, '/goodsregistry')
api.add_resource(GetBarang, '/getowngoods')
api.add_resource(GetAllBarang, '/getallgoods')
api.add_resource(RegistSertif, '/certificateregistry')
api.add_resource(PutSertif, '/goodscertification')
api.add_resource(CekBarang, '/originalchecking')
api.add_resource(PassChange, '/passchange')

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0", port=5000)

