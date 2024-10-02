from flask_restful import Resource, reqparse
from restdemo.model.daily_info import Dailyinfo
from restdemo.model.users import Users


class User_All_Data(Resource):
    def get(self,id):
        """
        get user detail information and all daily info
        """
        user = Users.query_by_id(id)
        if user:
            user_all_data = user.as_dict()
            # print("1:",user_all_data)
            # print("2:",user.daily_info)
            dailyinfos = user.daily_info
            daily_info = [dailyinfo.as_dict() for dailyinfo in dailyinfos]
            print(daily_info)
            user_all_data.update({"daily_info" : daily_info})
            return user_all_data
        return {'message': 'user not found'}, 404