# !/usr/bin/env python
# -*- coding: utf-8 -*-
__FileName__ = 'manager.py'
__author__ = 'chen_87217@126.com'
__date__ = '2020/3/13 0013 19:32'

from apps import app

from apps.views import user
from flask_script import Manager

if __name__ == '__main__':

    # 将蓝图对象注册到flask 服务中
    '''
    url_prefix:子路由前缀
    '''
    app.register_blueprint(user.blue, url_prefix="/user")

    # 以脚本的方式启动flask应用服务
    manager = Manager(app)
    manager.run()