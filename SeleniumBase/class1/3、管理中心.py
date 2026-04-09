import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import random

url = r"http://www.mall.com/admin/privilege.php?act=login"
serv = Service("chromedriver.exe")
driver = webdriver.Chrome(service=serv)
driver.maximize_window()
driver.get(url)
driver.implicitly_wait(10)

driver.find_element(By.NAME,'username').send_keys('admin')
driver.find_element(By.NAME,'password').send_keys('admin888')
driver.find_element(By.CLASS_NAME,'button').click()
time.sleep(1)
driver.switch_to.frame('header-frame')
driver.find_element(By.XPATH,'//*[@id="menu-div"]/ul/li[7]/a').click()
driver.switch_to.default_content()
driver.switch_to.frame('main-frame')
driver.find_element(By.XPATH,'/html/body/div[1]/form/input[3]').send_keys('abcde99')
driver.find_element(By.XPATH,'/html/body/div[1]/form/input[4]').click()
time.sleep(2)
driver.quit()

