import requests
import unittest
from MallApi.conf.config import leaving_url
from unittestreport import ddt,yaml_data
from MallApi.cookie.cookies import lion_cookie

# 留言
@ddt
class Leave(unittest.TestCase):
    def setUp(self):pass
    def tearDown(self):pass

    @yaml_data(r"D:\python\pythonBase\MallApi\data\leave_msg.yaml")
    def test_leave_msg(self,yaml_data):
        url, date = leaving_url, yaml_data['leave_msg_data']
        cookie = lion_cookie()
        rep = requests.post(url=url, data=date,cookies=cookie)
        self.assertIn(yaml_data['expect_val'], rep.text)

if __name__ == '__main__':
    unittest.main()