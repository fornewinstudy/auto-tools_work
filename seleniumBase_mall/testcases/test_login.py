import unittest
from unittestreport import ddt, yaml_data
from PO.public.login import login


@ddt
class Login(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        self.driver.quit()

    @yaml_data(r"D:\python\pythonBase\PO\data\login.yaml")
    def test_login(self,yaml_data):
        self.driver = login(yaml_data['name'],yaml_data['passwd'])
        if yaml_data["name"] == "" or yaml_data['passwd'] == '':
            self.assertIn(yaml_data['expect_val'], self.driver.switch_to.alert.text)
        else:
            self.assertIn(yaml_data['expect_val'],self.driver.page_source)

if __name__ == '__main__':
    unittest.main()