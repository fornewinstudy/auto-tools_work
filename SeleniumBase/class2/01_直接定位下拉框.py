#!/usr/bin/env python3
# @Time : 2026/2/4 09:03
# @Author : 潘璐璐
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

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
driver.find_element(By.NAME,"province").send_keys("广东")
sleep(2)
driver.find_element(By.NAME,"city").send_keys("深圳")
sleep(2)
driver.find_element(By.NAME,"district").send_keys("龙岗区")
sleep(2)
driver.quit()
