from datetime import datetime

from flask_restful import Resource
from models.food import FoodModel


class Food(Resource):
    def get(self, date):
        try:
            datetime.strptime(date, '%d-%m-%Y')
        except ValueError:
            return {'message': "Your date format is incorect. Example: 25/03/2018"}, 400

        result = {'food': FoodModel.get_food_by_date(date)}
        return result , 200
