import unittest
from unittestreport import ddt, yaml_data
from PO.public.addtocart import addtocart
import os,sys


@ddt
class Address(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        self.driver.quit()

    @yaml_data(r"")
    def test_address(self):
        self.driver = addtocart()


if __name__ == '__main__':
    unittest.main()