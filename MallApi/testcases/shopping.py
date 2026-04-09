import requests
import unittest
from MallApi.conf.config import shopping_url
from unittestreport import ddt,yaml_data
from MallApi.cookie.cookies import lion_cookie
from MallApi.cookie.query_name import query

#加入购物车
@ddt
class Shopping(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    @yaml_data(r"D:\python\pythonBase\MallApi\data\add_to_cart.yaml")
    def test_shopping(self,yaml_data):
        url= shopping_url
        sq=query()
        add_to_cart_data={
            "goods": f'{{"quick":1,"spec":[],"goods_id":{sq},"number":"{yaml_data['num']}","parent":0}}'
        }
        cookie = lion_cookie()
        rep = requests.post(url=url,data=add_to_cart_data,cookies=cookie)
        self.assertIn(yaml_data['expect_val'],rep.text)
        print(rep.text)

if __name__ == '__main__':
    unittest.main()
