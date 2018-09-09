import os
from datetime import datetime

from pymongo import MongoClient
from apscheduler.schedulers.background import BackgroundScheduler

client = MongoClient(os.environ['MONGO_URL'])
db = client.letifood_db


def update_week_number():
    record = db.week
    curson = record.find_one()

    if curson['week'] == 4:
        val_updated = 1
    else:
        val_updated = curson['week'] + 1
    db.week.update_one(
        {
            'week': curson['week']
        },
        {
            '$set': {
                'week': val_updated
            }

        }
    )


scheduler = BackgroundScheduler()
scheduler.add_job(update_week_number, 'cron', day_of_week=6, hour=23)
scheduler.start()


class FoodModel:

    @classmethod
    def get_food_by_date(cls, date):
        try:
            week_cursor = db.week.find_one()
            date_to_week = datetime.strptime(date, '%d-%m-%Y').weekday()
            if datetime.now().weekday() == 6 and date_to_week == 0:
                if week_cursor["week"] == 4:
                    weeknumber = 1
                else:
                    weeknumber = curson['week'] + 1
                curson = db.foodmenu.find({"week": weeknumber, "day_number": date_to_week})
            else:
                curson = db.foodmenu.find({"week": week_cursor["week"],"day_number":date_to_week})
            return {'lunch': curson[0]['lunch'], 'dinner': curson[0]['dinner']}
        except IndexError:
            return 'not found'
