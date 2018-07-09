#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-22 19:12:17
# @Author  : wushilong
# @Email   : 1320185818@qq.com | longofo.wu@gmail.com
# @Link    : http://longofo.cc

import os


class Config:
    # os.environ.get('SECRET_KEY') or 'hard to guess string'
    SECRET_KEY = os.urandom(24)
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
    FLASKY_PER_PAGE = int(os.environ.get('FLASKY_PER_PAGE' or 20))

    MONGO_URI = os.environ.get(
        'MONGO_URI') or 'mongodb://127.0.0.1:27017/zhihu'

    PAGE_SIZE = 20

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    Testing = True


class ProductionConfig(Config):

    @classmethod
    def init_app(cls, app):
        Config.init(app)


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
