#!/usr/bin/env python3
# @Time : 2026/2/4 14:07
# @Author : 潘璐璐
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service = Service("chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("http://www.mall.com/goods.php?id=16")
driver.maximize_window()
driver.implicitly_wait(10)
# 前端对于某个个别元素会有一个焦点操作，如果直接清空购物车数量，会让元素失去焦点，从而页面弹出告警框
# 如果直接使用send_keys()，会在原有的数字后面加上字符，并不是用户想要购买的真实数量
driver.find_element(By.ID,"number").send_keys(Keys.BACKSPACE)   # 调用键盘的回退键，删除数目
driver.find_element(By.ID,"number").send_keys("5")   # 调用键盘的回退键，删除数目
sleep(5)
driver.quit()
