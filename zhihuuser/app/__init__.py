#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-22 19:12:17
# @Author  : wushilong
# @Email   : 1320185818@qq.com | longofo.wu@gmail.com
# @Link    : http://longofo.cc

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_pymongo import PyMongo

from config import config, Config


bootstrap = Bootstrap()
mongo = PyMongo(config_prefix='MONGO')


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    mongo.init_app(app)

    with app.app_context():
        mongo.db['user'].drop_indexes()
        mongo.db['user'].create_index(
            [('name', 'text'), ('headline', 'text'), ('url_token', 'text')])

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
