import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import random

class FullLink():
    def __init__(self):
        self.url = "http://www.mall.com/user.php"
        self.serv = Service("chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.serv)
        self.driver.maximize_window()
        self.driver.get(self.url)
        self.driver.implicitly_wait(10)


    def signin(self):
        self.driver.find_element(By.NAME, "username").send_keys('aaa')
        self.driver.find_element(By.NAME, "password").send_keys('123456')
        self.driver.find_element(By.NAME, "submit").click()
        assert "登录成功" in self.driver.page_source

    def search(self,name):
        self.driver.find_element(By.ID, "keyword").send_keys(name)
        self.driver.find_element(By.XPATH, "//*[@class='sea_submit']").click()
        self.driver.find_element(By.XPATH, '//*[@class="productimg"]').click()
        self.driver.find_element(By.XPATH, '//*[@class="iconfont"]').click()
        randoms =  self.driver.find_elements(By.XPATH,'//*[@class="productimg"]/img')
        random.choice(randoms).click()


    def settlement(self):
        self.headles = self.driver.window_handles  # 获取全部窗口
        self.driver.switch_to.window(self.headles[-1])  # 最新窗口
        # time.sleep(10)
        self.driver.find_element(By.XPATH, '//*[@id="buy_btn"]').click()
        # time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@class="go"]/a[2]').click()
        self.driver.find_element(By.XPATH, '//*[@class="btn"]').click()

    def addAddress(self):
        if "收货人信息" in self.driver.page_source:
            driver = self.driver.find_elements(By.XPATH, '//*[@name="province"]/option')
            driver.pop(0)
            random.choice(driver).click()
            time.sleep(1)
            driver1 = self.driver.find_elements(By.XPATH, '//*[@id="selCities_0"]/option')
            driver1.pop(0)
            random.choice(driver1).click()
            time.sleep(1)
            driver2 = self.driver.find_elements(By.XPATH, '//*[@id="selDistricts_0"]/option')
            driver2.pop(0)
            random.choice(driver2).click()
            self.driver.find_element(By.XPATH, '//*[@name="consignee"]').send_keys('张三')
            self.driver.find_element(By.XPATH, '//*[@id="address_0"]').send_keys('深圳龙岗坂田')
            self.driver.find_element(By.XPATH, '//*[@id="mobile_0"]').send_keys('13033453189')
            self.driver.find_element(By.XPATH, '//*[@class="btn"]').click()
        else:
            pass

    def submit(self):
        self.driver.find_element(By.XPATH, '//*[@align="center"]/input[@value="3"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="pay_check_value_2"]').click()
        self.driver.find_element(By.XPATH, '//*[@type="image"]').click()
        self.driver.switch_to.window(self.headles[0])  # 最新窗口
        time.sleep(2)
        self.driver.quit()



if __name__ == '__main__':
    driver = FullLink()
    driver.signin()
    driver.search('水果')
    driver.settlement()
    # driver.addAddress()
    driver.submit()

