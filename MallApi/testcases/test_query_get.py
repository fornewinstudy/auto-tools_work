import requests
import unittest
from unittestreport import ddt, yaml_data
from MallApi.conf.config import query_get_url
from MallApi.cookie.login_token import toke

@ddt
class Query_get(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass

    @yaml_data(r"D:\python\pythonBase\MallApi\data\query_get.yaml")
    def test_query_get(self,yaml_data):
        url,parm = query_get_url,yaml_data['param']
        header = toke()
        req = requests.get(url=url,params=parm,headers=header)
        self.assertIn(yaml_data['expect_val'],req.text)

if __name__ == '__main__':
    unittest.main()


