from flask_restful import Resource, reqparse
from models.user import UserModel


class User(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('alert',
                        type=bool,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('bot',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )

    def get(self, fid):
        return {'message': UserModel.user_exist(fid)}, 200

    def post(self, fid):
        data = User.parser.parse_args()
        if UserModel.user_exist(fid):
            return {'message': 'User already exist.'}, 400
        if UserModel.save_new_user(fid, data):
            return {"message": "success"}, 201
        else:
            return {"message": "failed"}, 500

    def put(self, fid):
        data = User.parser.parse_args()
        if not UserModel.user_exist(fid):
            return {'message': 'Can\'t find user.'}, 400
        if UserModel.update_user_alert(fid, data):
            return {"message": "success"}, 200
        else:
            return {"message": "failed"}, 500


class UserList(Resource):
    def get(self, scope):
        return {'users': UserModel.get_all_users_alert(scope)}, 200