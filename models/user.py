import os

from pymongo import MongoClient

client = MongoClient(os.environ['MONGO_URL'])
db = client.letifood_db



class UserModel:

    @classmethod
    def save_new_user(cls, fid, data):
        try:
            db.users.insert({
                "fid": fid,
                "alert": data.alert,
                "bot": data.bot
            }
            )
            return True
        except IndexError:
            return False

    @classmethod
    def update_user_alert(cls, fid, data):
        try:
            db.users.update_one(
                {
                    'fid': fid
                },
                {
                    '$set': {
                        'alert': data.alert
                    }

                }
            )
            return True
        except IndexError:
            return False

    @classmethod
    def user_exist(cls, fid):
        try:
            curson = db.users.find(
                {
                    "fid": fid
                }
            )
            if curson.count() > 0:
                return True
            else:
                return False
        except IndexError:
            return True

    @classmethod
    def get_all_users_alert(cls,scope):
        try:
            curson = db.users.find(
                {
                    "alert": True,
                    "bot": scope
                }
            )
            if curson.count() > 0:
                data = []
                for user in curson:
                    data.append({
                        "fid": user["fid"]
                    })
                return data
            else:
                return False
        except IndexError:
            return True
