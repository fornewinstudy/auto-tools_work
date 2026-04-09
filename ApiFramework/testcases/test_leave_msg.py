#!/usr/bin/env python3
# @Time : 2026/1/30 15:34
# @Author : 潘璐璐
import unittest
import requests
from ApiFramework.conf.config import LeaveMsgUrl
from ApiFramework.public.get_cookie import get_cookie
from unittestreport import ddt,yaml_data

@ddt
class LeaveMsq(unittest.TestCase):

    def setUp(self):pass

    def tearDown(self):pass

    @yaml_data(r"D:\PythonProject\109\ApiFramework\data\leave_msg.yaml")
    def test_leave_msg(self,yaml_data):
        url,leave_msg_data = LeaveMsgUrl,yaml_data["leave_msg_data"]
        cookie = get_cookie()   # 调用封装好的函数，获取登录成功的cookie信息
        resp = requests.post(url,data=leave_msg_data,cookies=cookie)
        self.assertIn(yaml_data["expect_val"],resp.text)


if __name__ == '__main__':
    unittest.main()
