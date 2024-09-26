from flask_restful import Resource, reqparse
from restdemo.model.users import Users as UserModel

class User(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'name', type=str, required=False,
        help='{error_msg}'
    )
    parser.add_argument(
        'gender',type=str, required=False,
        help='{error_msg}'
    )
    parser.add_argument(
        'age', type=int, required=False,
        help='{error_msg}'
    ) 
    parser.add_argument(
        'weight', type=float, required=False,
        help='{error_msg}'
    )
    parser.add_argument(
        'height', type=float, required=False,
        help='{error_msg}'
    )    
    parser.add_argument(
        'activity_level', type=float, required=False,
        help='{error_msg}'
    ) 
    parser.add_argument(
        'meta', type=int, required=False,
        help='{error_msg}'
    )       
    # def get(self, username):
    #     """
    #     get user detail information
    #     """
    #     print(username)
    #     user = UserModel.query_by_username(username)
         
    #     if user:
    #         return user.as_dict()
    #     return {'message': 'user not found'}, 404

    def get(self, id):
        """
        get user detail information
        """
        print(id)
        data = User.parser.parse_args()
        if data.get('meta') == 1:
            col_list = UserModel.get_metadata()
            return {i: col_list[i] for i in range(len(col_list))}
        
        user = UserModel.query_by_id(id)
         
        if user:
            return user.as_dict()
        return {'message': 'user not found'}, 404
    
    def post(self, id):
        """ create a user"""
        # print(request.get_json())
        data = User.parser.parse_args()

        user = UserModel.query_by_id(id)
        if not user:
            user = UserModel( u_id = id,
                                name=data.get('name'),
                                gender=data.get('gender'),
                                age=data.get('age'),
                                weight=data.get('weight'),
                                height=data.get('height'),
                                activity_level=data.get('activity_level'),
                                )
            user.add()
            return user.as_dict(), 201
        return {'message': 'user already exist'}

    
    def delete(self, id):
        """delete user"""
        user = UserModel.query_by_id(id)
        if user:
            user.delete()
            # db.session.delete(user)
            # db.session.commit()
            return user.as_dict(), 201
        return {'message': 'user not found'},204
    
    def put(self, id):
        """update user"""
        data = User.parser.parse_args()
        user = UserModel.query_by_id(id)
        if user:
            if data.get('name'):
               user.name = data.get('name')  
            if data.get('gender'):
               user.gender = data.get('gender')         
            if data.get('age'):
                user.age=data.get('age')
            if data.get('weight'):            
                user.weight=data.get('weight')
            if data.get('height'):   
                user.height=data.get('height')
            if data.get('activity_level'):               
                user.activity_level=data.get('activity_level')   
            user.update()
            return user.as_dict(), 201
        return {'message': 'user not found'},204
    



class UserList(Resource):
  
    def get(self):

        users = UserModel.get_user_list()
        return [user.as_dict() for user in users]
