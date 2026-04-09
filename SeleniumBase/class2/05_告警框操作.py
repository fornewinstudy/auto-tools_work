#!/usr/bin/env python3
# @Time : 2026/2/4 11:30
# @Author : 潘璐璐
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get(r"D:\PythonProject\109\SeleniumBase\Day2\Alert.html")
driver.maximize_window()
driver.implicitly_wait(10)
# 点击第一种弹窗
driver.find_element(By.XPATH,"/html/body/div/button[1]/h3").click()
sleep(2)
# 获取弹窗的文本值
print(driver.switch_to.alert.text)
# 弹窗中点击确定按钮
driver.switch_to.alert.accept()
sleep(2)

# 点击第二种弹窗
driver.find_element(By.XPATH,"/html/body/div/button[2]/h3").click()
sleep(2)
driver.switch_to.alert.send_keys("你好！同学们")
sleep(2)
driver.switch_to.alert.accept() # 点击确定
sleep(2)
driver.switch_to.alert.accept() # 再次点击确定

# 点击第三种弹窗
driver.find_element(By.XPATH,"/html/body/div/button[3]/h3").click()
sleep(2)
driver.switch_to.alert.dismiss()    # 弹窗中点击取消
sleep(2)
driver.quit()
