from flask import Flask
from flask_restful import Api

from resources.food import Food
from resources.user import User, UserList

app = Flask(__name__)
api = Api(app)

api.add_resource(Food, '/api/v1/food/<string:date>')

api.add_resource(UserList, '/api/v1/users/<string:scope>')
api.add_resource(User, '/api/v1/user/<string:fid>')

if __name__ == '__main__':
    app.run(port=8000)
