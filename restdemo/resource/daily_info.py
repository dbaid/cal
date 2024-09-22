from flask_restful import Resource, reqparse
from restdemo.model.daily_info import Dailyinfo as dailymodel
from restdemo.model.users import Users 
from datetime import datetime, timedelta

class Dailyinfo(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'date', type=str, 
        help='{error_msg}'
    )
    parser.add_argument(
        'time', type=str, 
        help='{error_msg}'
    )
    parser.add_argument(
        'food_name', type=str, 
        help='{error_msg}'
    )   
    parser.add_argument(
        'food_calories', type=float, 
        help='{error_msg}'
    )
    parser.add_argument(
        'exercise_name', type=str, 
        help='{error_msg}'
    )
    parser.add_argument(
        'exercise_duration', type=float, 
        help='{error_msg}'
    )
    parser.add_argument(
        'days_before', type=int, 
        help='{error_msg}'
    )

    parser.add_argument(
        'weight_target', type=float, 
        help='{error_msg}'
    )

    parser.add_argument(
        'bmr_target', type=float, 
        help='{error_msg}'
    )

    parser.add_argument(
        'calories_burned', type=float, 
        help='{error_msg}'
    )


    def get(self, id):
        data = Dailyinfo.parser.parse_args()
        days_before = data.get('days_before')
        user = Users.query_by_id(id)
        if user:
            dailyinfos = user.daily_info
            return [dailyinfo.as_dict() for dailyinfo in dailyinfos if datetime.strptime(dailyinfo.date, "%y-%m-%d").date() >= (datetime.today().date() - timedelta(days=days_before))]
        return {'message': 'user not found'}, 404

    def post(self,id):
        data = Dailyinfo.parser.parse_args()
        user = Users.query_by_id(id)
        print(user)
        print(data)
        if user:
            dailyinfo = dailymodel(u_id = user.u_id,
                                  date=data.get('date'),
                                  time=data.get('time'),
                                  food_name=data.get('food_name'), 
                                  food_calories=data.get('food_calories'),
                                  exercise_name=data.get('exercise_name'),
                                  exercise_duration=data.get('exercise_duration'),
                                  weight_target=data.get('weight_target'),
                                  bmr_target=data.get('bmr_target'),
                                  calories_burned=data.get('calories_burned')                                  
                                )
            dailyinfo.add()
            return dailyinfo.as_dict(), 201
        return {'message': 'user not found'}, 404

