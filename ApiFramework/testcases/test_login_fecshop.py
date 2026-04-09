#!/usr/bin/env python3
# @Time : 2026/1/31 15:18
# @Author : 潘璐璐
import unittest
import requests
from unittestreport import ddt,yaml_data
from ApiFramework.conf.config import FecshopLoginUrl

@ddt
class LoginFecshop(unittest.TestCase):

    def setUp(self):pass

    def tearDown(self):pass

    @yaml_data(r"D:\PythonProject\109\ApiFramework\data\login_fecshop.yaml")
    def test_login_fecshop(self,yaml_data):
        url,json_data = FecshopLoginUrl,yaml_data["json_data"]
        resp = requests.post(url,json=json_data)
        self.assertIn(yaml_data["expect_val"],resp.text)


if __name__ == '__main__':
    unittest.main()