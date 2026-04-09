#!/usr/bin/env python3
# @Time : 2026/1/31 09:05
# @Author : 潘璐璐
import unittest

import requests
from unittestreport import ddt, yaml_data

# from MallApi.conf.config import AddToCartUrl
# from MallApi.public.get_cookie import get_cookie
# from MallApi.public.get_goods_id import get_gid


@ddt
class AddToCart(unittest.TestCase):

    def setUp(self): pass

    def tearDown(self): pass

    @yaml_data(r"D:\PythonProject\109\MallApi\data\add_to_cart.yaml")
    def test_add_to_cart(self, yaml_data):
        url = AddToCartUrl
        gid = get_gid()
        add_to_cart_data = {
            "goods": f'{{"quick":1,"spec":[],"goods_id":{gid},"number":"{yaml_data['num']}","parent":0}}'
        }
        resp = requests.post(url, data=add_to_cart_data, cookies=get_cookie())
        self.assertIn(yaml_data["expect_val"], resp.text)


if __name__ == '__main__':
    unittest.main()
