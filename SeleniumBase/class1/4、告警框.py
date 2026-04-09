import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import random


url = r"D:\python\pythonBase\SeleniumBase\Day1\Alert.html"
serv = Service("chromedriver.exe")
driver = webdriver.Chrome(service=serv)
driver.maximize_window()
driver.get(url)
driver.implicitly_wait(10)
# 第一种弹窗
driver.find_element(By.XPATH,'/html/body/div/button[1]').click()
# 弹窗中点击确定按钮
time.sleep(2)
driver.switch_to.alert.accept()
time.sleep(2)
# 第二种弹窗
driver.find_element(By.XPATH,'/html/body/div/button[2]').click()
time.sleep(2)
# 在弹窗中输入内容
driver.switch_to.alert.send_keys('你好同学')
time.sleep(2)
driver.switch_to.alert.accept() #点击确定
driver.switch_to.alert.accept() #再次点击确定

# 第三种弹窗
driver.find_element(By.XPATH,'/html/body/div/button[3]').click()
time.sleep(2)
driver.switch_to.alert.dismiss() #点击取消
driver.quit()























