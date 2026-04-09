import requests
import unittest
from Fecshop.conf.Url import Login_Url
from unittestreport import ddt,yaml_data

@ddt
class Login(unittest.TestCase):
    def setUp(self):pass
    def tearDown(self):pass
    @yaml_data(r"C:\Users\Administrator\Desktop\pycharm\Fecshop\data\login.yaml")
    def test_login(self,yaml_data):
        url = Login_Url
        date = yaml_data['date']
        rep = requests.post(url=url,json=date)
        self.assertIn(yaml_data['expect_val'],rep.text)

if __name__ == '__main__':
    unittest.main()