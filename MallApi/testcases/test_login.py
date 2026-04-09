import requests
import unittest
from MallApi.conf.config import lion_url
from unittestreport import ddt,yaml_data


@ddt
class Demo(unittest.TestCase):
    def setUp(self):pass
    def tearDown(self):pass
#登入
    @yaml_data(r"D:\python\pythonBase\MallApi\data\login.yaml")
    def test_loin(self,yaml_data):
        # print(yaml_data)
        url,date = lion_url,yaml_data ['login_date']
        rep = requests.post(url=url,data=date)
        self.assertIn(yaml_data ['expect_val'],rep.text)


if __name__ == '__main__':
    unittest.main()