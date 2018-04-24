from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from user import UserRegister
from item import Items, ItemList

app = Flask(__name__)
app.secret_key = 'Sai'
api = Api(app)

jwt = JWT(app, authenticate, identity)   # creates a new endpoint /auth

api.add_resource(Items, '/item/<string:name>')    #http://localhost:5000/student/Sai
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
