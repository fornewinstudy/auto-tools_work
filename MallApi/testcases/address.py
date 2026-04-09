import requests
import unittest
from MallApi.cookie.cookies import lion_cookie
from unittestreport import ddt, yaml_data
from MallApi.conf.config import addres_url

# 添加收货地址
@ddt
class Addres(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @yaml_data(r"D:\python\pythonBase\MallApi\data\address.yaml")
    def test_addres(self,yaml_data):
        url,addres_data = addres_url,yaml_data['addres_data']
        cookie = lion_cookie()
        req = requests.post(url=url,data=addres_data,cookies=cookie)
        self.assertIn(yaml_data['expect_val'],req.text)
if __name__ == '__main__':
    unittest.main()
