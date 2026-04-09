import unittest
from unittestreport import ddt, yaml_data
from PO.public.query import Query


@ddt
class Login(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        self.driver.quit()

    @yaml_data(r"D:\python\pythonBase\PO\data\query_goods.yaml")
    def test_login(self,yaml_data):
        self.driver = Query(yaml_data["name"])
        if yaml_data["name"] == "":
            self.assertIn(yaml_data['expect_val'], self.driver.switch_to.alert.text)
        else:
            self.assertIn(yaml_data['expect_val'],self.driver.page_source)

if __name__ == '__main__':
    unittest.main()