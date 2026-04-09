import requests
import unittest
from unittestreport import ddt, yaml_data
from MallApi.conf.config import token_url


@ddt
class Token(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @yaml_data(r"D:\python\pythonBase\MallApi\data\aftoken.yaml")
    def test_query(self, yaml_data):
        url, json_data = token_url, yaml_data['json_data']
        res = requests.post(url=url, json=json_data)
        self.assertIn(yaml_data['expect'], res.text)


if __name__ == '__main__':
    unittest.main()
