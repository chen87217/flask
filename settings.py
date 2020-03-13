# !/usr/bin/env python
# -*- coding: utf-8 -*-
__FileName__ = 'settings.py'
__author__ = 'chen_87217@126.com'
__date__ = '2020/3/13 0013 19:34'

import os

from redis import Redis


class Dev():
    ENV = 'development'
    BASE_ROOT = os.path.dirname(os.path.abspath(__file__))

    SECRET_KEY = 'chen2342f'

    # 配置 flask-session
    SESSION_TYPE = 'redis'
    SESSION_REDIS = Redis(host='127.0.0.1', db=9)


    # mysql数据库配置
    HOST = '127.0.0.1'
    PORT = '3308'
    DATABASE = 'flaskdb'
    USERNAME = 'root'
    PASSWORD = ''
    CHARSET = 'utf8'

    DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset={charset}" \
        .format(username=USERNAME, password=PASSWORD, host=HOST, port=PORT, db=DATABASE, charset=CHARSET)

    SQLALCHEMY_DATABASE_URI = DB_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True