from flask import Flask
import os
import configparser
from flask_sqlalchemy import SQLAlchemy

config_parser = configparser.ConfigParser()
config_parser.read('config.ini')
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile('config.py')
    app.config['SECRET_KEY'] = config_parser['DEFAULT']['SECRET_KEY']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from app.views.home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    return app