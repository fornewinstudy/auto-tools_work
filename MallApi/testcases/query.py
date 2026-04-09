import unittest
import requests
from unittestreport import ddt,yaml_data
from MallApi.conf.config import query_url
from MallApi.cookie.cookies import lion_cookie
import random

#查询
@ddt
class  Query(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    @yaml_data(r"D:\python\pythonBase\MallApi\data\query.yaml")
    def test_query(self,yaml_data):
        url,query_data = query_url,yaml_data["query_data"]
        cookie = lion_cookie()
        req = requests.get(url=url,params=query_data,cookies=cookie)
        self.assertIn(yaml_data['expect_val'],req.text)
        print(req.text)

if __name__ == '__main__':
    unittest.main()








