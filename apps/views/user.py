# !/usr/bin/env python
# -*- coding: utf-8 -*-
__FileName__ = 'user.py'
__author__ = 'chen_87217@126.com'
__date__ = '2020/3/13 0013 19:47'

import os
import hashlib
from datetime import datetime

from flask import Blueprint, url_for, render_template
from flask import request, Response, make_response, redirect, jsonify, session

from settings import Dev
from models import db, user


blue = Blueprint('userBlue', __name__, template_folder='templates')


@blue.route('/', methods=('GET',))
def index():
    curruser = session.get('user', None)
    if curruser is None:
        return redirect('login')
        # return redirect(url_for('userBlue.login'))
    else:
        return '当前用户:%s' % curruser['username']


@blue.route('/find/<int:id>', methods=('GET',))
def find(id):
    row = user.User.query.get(id)
    if row:
        message = 'OK'
    else:
        message = 'Not Found'
    return jsonify({
      'status': 200,
      'message': message,
      'data': row
    })


@blue.route('/do', methods=('GET', 'POST'))
def center():
    return "进入到用户信息"


@blue.route('add', methods=('GET',))
def add():
    # username = '陈祥'
    # pwd = hashlib.md5('123456'.encode('utf-8')).hexdigest()
    u = user.User()
    u.username = '陈乾坤'
    u.email = 'chen_87217@126.com'
    db.session.add(u)
    session['user'] = u
    db.session.commit()
    return Response('添加成功')


@blue.route('/delete/<int:id>', methods=('DELETE',))
def delete():
    id = request.form.get('id')
    return "删除用户"


@blue.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'GET':
        html = render_template('login.html')
        return html
    else:
        username = request.form.get('username', None)
        pwd = request.form.get('pwd', None)

        if all((username, pwd)):
            response = make_response('cookie保存操作')
            expire_datetime = datetime.strptime('2020-3-11 15:04:01', '%Y-%m-%d %H:%M:%S')
            response.set_cookie('user', username, expires=expire_datetime)
            return response
        else:
            data = '{"message": "用户名和密码不能为空"}'
            code = 200
            # return Response(data, code, content_type='application/json')

            response = make_response(data, code)
            response.headers['Content-type'] = 'application/json'
            return response


@blue.route('/logout', methods=('GET',))
def logout():
    response = Response('用户注销')
    response.delete_cookie('user')
    return response