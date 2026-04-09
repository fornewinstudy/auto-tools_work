#!/usr/bin/env python3
# @Time : 2026/2/4 09:32
# @Author : 潘璐璐
import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("http://www.mall.com/user.php")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.NAME, "username").send_keys("qqq")
driver.find_element(By.NAME, "password").send_keys("123456")
driver.find_element(By.NAME, "submit").click()
driver.find_element(By.LINK_TEXT, "会员中心").click()
driver.find_element(By.LINK_TEXT, "收货地址").click()
# 第一步获取所有的省份元素对象
provinces = driver.find_elements(By.XPATH, "//select[@name='province']/option")
# 由于下拉框中的默认值为【请选择省】，需要将其去除
provinces.pop(0)
random.choice(provinces).click()
sleep(2)
cities = driver.find_elements(By.XPATH, "//select[@name='city']/option")
# 由于下拉框中的默认值为【请选择市】，需要将其去除
cities.pop(0)
random.choice(cities).click()
sleep(2)
districts = driver.find_elements(By.XPATH, "//select[@name='district']/option")
# 由于下拉框中的默认值为【请选择市】，需要将其去除
districts.pop(0)
random.choice(districts).click()
sleep(2)
driver.quit()
