#!/usr/bin/env python3
# @Time : 2026/1/31 16:21
# @Author : 潘璐璐
import unittest
import requests
from unittestreport import ddt,yaml_data
from ApiFramework.conf.config import QueryGoodsListUrl
from ApiFramework.public.get_token import get_token

@ddt
class QueryGoodsList(unittest.TestCase):

    def setUp(self):pass

    def tearDown(self):pass

    @yaml_data(r"D:\PythonProject\109\ApiFramework\data\query_goods_list.yaml")
    def test_query_goods_list(self,yaml_data):
        url ,param= QueryGoodsListUrl,yaml_data["param"]
        header = get_token()
        resp = requests.get(url,params=param,headers=header)
        self.assertIn(yaml_data["expect_val"],resp.text)


if __name__ == '__main__':
    unittest.main()
