from flask import Flask
from flask_restful import  Api
from restdemo.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
from restdemo.resource.user import User, UserList
from restdemo.resource.daily_info import Dailyinfo



def create_app():
    app = Flask(__name__)
    api = Api(app)
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///demo.db'
    app.config.from_object(Config)
    db.init_app(app)
    migrate = Migrate(app, db)



    # api.add_resource(Helloworld, '/')
    # api.add_resource(User, '/user/<string:username>')
    api.add_resource(User, '/user/<string:id>')   
    # api.add_resource(UserList, '/users')
    api.add_resource(Dailyinfo, '/dailyinfo/<string:id>')
    
    return app
