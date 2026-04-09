#!/usr/bin/env python3
# @Time : 2026/2/4 09:09
# @Author : 潘璐璐
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service = Service("chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("http://www.mall.com/user.php")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.NAME,"username").send_keys("qqq")
driver.find_element(By.NAME,"password").send_keys("123456")
driver.find_element(By.NAME,"submit").click()
driver.find_element(By.LINK_TEXT,"会员中心").click()
driver.find_element(By.LINK_TEXT,"收货地址").click()
# 第一步定位到需要操作的下拉框
province = driver.find_element(By.NAME,"province")
# 第二步调用Select类提供的方法来操作下拉框
Select(province).select_by_value("7")
sleep(2)
# 第一步定位到需要操作的下拉框
city= driver.find_element(By.NAME,"city")
Select(city).select_by_index(2)
sleep(2)
# 第一步定位到需要操作的下拉框
district = driver.find_element(By.NAME,"district")
# 第二步调用Select类提供的方法来操作下拉框
Select(district).select_by_visible_text("阳朔县")
sleep(2)
driver.quit()
