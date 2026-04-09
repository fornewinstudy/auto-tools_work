import requests
import unittest
from MallApi.conf.config import shopping_url
from unittestreport import ddt,yaml_data
from MallApi.cookie.cookies import lion_cookie
from MallApi.cookie.query_name import query

@ddt
class Sett(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    @yaml_data('')
    def test_sett(self,yaml_data):
        pass