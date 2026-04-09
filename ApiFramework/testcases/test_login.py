#!/usr/bin/env python3
# @Time : 2026/1/30 14:37
# @Author : 潘璐璐
import unittest
import requests
from unittestreport import ddt, yaml_data
from ApiFramework.conf.config import LoginUrl


@ddt  # @ddt是装饰器，装饰器的定义：是在不改变类或者函数调用方式的情况下，给类或者函数增加新的功能
class Login(unittest.TestCase):  # @ddt是用来装饰Login这个类，从而实现数据驱动

    def setUp(self): pass  # 初始化方法

    def tearDown(self): pass  # 结束化方法

    # @yaml_data装饰器会读取login.yaml文件中的内容然后赋值给变量yaml_data，且类型为字典
    @yaml_data(r"D:\PythonProject\109\ApiFramework\data\login.yaml")
    def test_login(self, yaml_data):
        url, login_data = LoginUrl, yaml_data["login_data"]  # 登录的接口地址和请求参数
        resp = requests.post(url, data=login_data)  # 发送登录接口请求
        self.assertIn(yaml_data["expect_val"], resp.text)


if __name__ == '__main__':
    unittest.main()
