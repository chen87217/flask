# !/usr/bin/env python
# -*- coding: utf-8 -*-
__FileName__ = 'test_user.py'
__author__ = 'chen_87217@126.com'
__date__ = '2020/3/13 0013 22:37'


import unittest
from unittest import TestCase

import requests


# 声明单元测试类
class TestUser(TestCase):
    # 声明单元测试方法
    # 方法名以"test_"开头
    def test_del(self):
        url = "127.0.0.1:5000/user/delete/4"
        methods = 'DELETE'
        resp = requests.request(methods, url)

        # resp = requests.delete(url)

        # 断言, 最后一个参数表示断言失败的消息
        self.assertIs(resp.status_code, 200, '请求失败')

        print(resp.text)


unittest.main()

