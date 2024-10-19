from flask import Flask
from flask_restful import  Api
from restdemo.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from restdemo.config import app_config

db = SQLAlchemy()
from restdemo.resource.user import User
from restdemo.resource.daily_info import Dailyinfo
from restdemo.resource.user_all_data import User_All_Data



def create_app(config_name='testing'):
    app = Flask(__name__)
    api = Api(app)
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///demo.db'
    app.config.from_object(app_config[config_name])
    db.init_app(app)
    migrate = Migrate(app, db)



    # api.add_resource(Helloworld, '/')
    # api.add_resource(User, '/user/<string:username>')
    api.add_resource(User, '/user/<string:id>')   
    # api.add_resource(UserList, '/users')
    api.add_resource(Dailyinfo, '/dailyinfo/<string:id>')
    api.add_resource(User_All_Data, '/useralldata/<string:id>')
    
    return app
