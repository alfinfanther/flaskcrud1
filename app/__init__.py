from flask import Flask
import os
import configparser

config_parser = configparser.ConfigParser()
config_parser.read('config.ini')

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile('config.py')
    app.config['SECRET_KEY'] = config_parser['DEFAULT']['SECRET_KEY']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    return app