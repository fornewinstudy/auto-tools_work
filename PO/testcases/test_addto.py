import unittest
from PO.public.addto import addto
from unittestreport import ddt, yaml_data


@ddt
class Addto(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        self.driver.quit()

    @yaml_data(r"D:\python\pythonBase\PO\data\address.yaml")
    def test_addtoer(self,yaml_data):
        self.driver = addto(yaml_data["name"],yaml_data["address"],
                            yaml_data["EM"],yaml_data["number"])
        # print(self.driver)
        if yaml_data['expect_val'] == "您的收货地址信息已成功更新！":
            self.assertIn(yaml_data['expect_val'], self.driver.page_source)
        else:
            self.assertIn(yaml_data['expect_val'], self.driver.switch_to.alert.text)

if __name__ == '__main__':
    unittest.main()