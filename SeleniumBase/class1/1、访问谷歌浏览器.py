# from keyword import kwlist
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.action_chains import ActionChains
import random

import time
url = "http://www.mall.com/user.php"
# print(requests.get(url))
# webbrowser.open_new("http://www.fangwei.com/index.php?ctl=user&act=login")
serv= Service("chromedriver.exe")
z = webdriver.Chrome(service=serv)
z.maximize_window()
z.get(url)
z.implicitly_wait(10)
z.find_element(By.NAME, "username").send_keys('aaa')
z.find_element(By.NAME, "password").send_keys('123456')
z.find_element(By.NAME, "submit").click()
# 断言，表示登录成功在返回的原始数据内
assert "登录成功" in z.page_source
z.find_element(By.ID,"keyword").send_keys("水果")
z.find_element(By.XPATH,"//*[@class='sea_submit']").click()
z.find_element(By.XPATH,'//*[@class="productimg"]').click()
z.find_element(By.XPATH,'//*[@class="iconfont"]').click()
xpath = '//*[@class="productimg"]/img[@title="四川双流草莓新鲜水果礼盒2盒"]'
z.find_element(By.XPATH,xpath).click()
#切换窗口
headles = z.window_handles #获取全部窗口
z.switch_to.window(headles[-1]) #最新窗口
# time.sleep(10)
z.find_element(By.XPATH,'//*[@id="buy_btn"]').click()
time.sleep(1)
z.find_element(By.XPATH,'//*[@class="go"]/a[2]').click()
z.find_element(By.XPATH,'//*[@class="btn"]').click()
# 方法一
# driver = z.find_element(By.XPATH,'//*[@name="province"]')
# driver.find_element(By.XPATH,'//*[@value="6"]').click()
# driver1 = z.find_element(By.XPATH,'//*[@id="selCities_0"]')
# driver1.find_element(By.XPATH,'//*[@value="77"]').click()
# driver2 = z.find_element(By.XPATH,'//*[@id="selDistricts_0"]')
# driver2.find_element(By.XPATH,'//*[@value="709"]').click()
# 方法二随机数
driver = z.find_elements(By.XPATH,'//*[@name="province"]/option')
driver.pop(0)
random.choice(driver).click()
time.sleep(1)
driver1 = z.find_elements(By.XPATH,'//*[@id="selCities_0"]/option')
driver1.pop(0)
random.choice(driver1).click()
time.sleep(1)
driver2 = z.find_elements(By.XPATH,'//*[@id="selDistricts_0"]/option')
driver2.pop(0)
random.choice(driver2).click()
z.find_element(By.XPATH,'//*[@name="consignee"]').send_keys('张三')
z.find_element(By.XPATH,'//*[@id="address_0"]').send_keys('深圳龙岗坂田')
z.find_element(By.XPATH,'//*[@id="mobile_0"]').send_keys('13033453189')
z.find_element(By.XPATH,'//*[@class="btn"]').click()
# z.switch_to.window(headles[-1])
z.find_element(By.XPATH,'//*[@align="center"]/input[@value="3"]').click()
z.find_element(By.XPATH,'//*[@id="pay_check_value_2"]').click()
z.find_element(By.XPATH,'//*[@type="image"]').click()
z.switch_to.window(headles[0]) #最新窗口
time.sleep(2)
z.quit()