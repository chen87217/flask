# !/usr/bin/env python
# -*- coding: utf-8 -*-
__FileName__ = 'migrate.py'
__author__ = 'chen_87217@126.com'
__date__ = '2020/3/13 0013 20:58'


from flask_script import Manager, Server
from apps import app
from flask_migrate import Migrate, MigrateCommand
from models import db, user


manager = Manager(app)
Migrate(app=app, db=db)
manager.add_command('db', MigrateCommand) # 创建数据库映射命令
manager.add_command('start', Server(port=8000, use_debugger=True)) # 创建启动命令

if __name__ == '__main__':
    manager.run()