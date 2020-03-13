# !/usr/bin/env python
# -*- coding: utf-8 -*-
__FileName__ = '__init__.py.py'
__author__ = 'chen_87217@126.com'
__date__ = '2020/3/13 0013 19:35'


import os
from flask import Flask, render_template, Response
from flask_session import Session

from flask_cors import CORS  # 跨域设置

import settings
from models import db


app = Flask(__name__)
app.debug = True

CORS(app, supports_credentials=True)
# cors = CORS(app, resources={r"/api/*": {"origins": "*"}})  # 允许所有域名跨域
# cors = CORS(app, resources={r"/.*": {"origins": "http://192.168.1.92:8081"}})   # 只允许特定域名跨域
# cors = CORS(app, resources={r"/.*": {"origins": ["http://192.168.1.92:8081","http://www.bai.com"]}})   # 只允许特定几个域名跨域


# 从指定的对象中加载flask服务的配置
app.config.from_object(settings.Dev())

# flask-session  创建 需要在加载配置之后才能创建
session = Session()
session.init_app(app)

# 初始化sqlalchemy对象
db.init_app(app)


# 自定义时间格式  过滤器
@app.template_filter('datefrm')
def datefrm(value, *args):
    from datetime import datetime
    return datetime.strftime(value, args[0])


@app.errorhandler(404)
def notfound(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def page_not_found(error):
    return render_template('500.html'), 500


@app.errorhandler(Exception)
def handererror(error):
    return render_template('error.html')