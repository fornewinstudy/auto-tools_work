#!/usr/bin/env python3
# @Time : 2026/2/4 10:27
# @Author : 潘璐璐
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("http://www.mall.com/admin/privilege.php?act=login")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.NAME, "username").send_keys("admin")
driver.find_element(By.NAME, "password").send_keys("admin888")
driver.find_element(By.CLASS_NAME, "button").click()
# 切换到frame里面
driver.switch_to.frame("header-frame")
driver.find_element(By.LINK_TEXT, "会员列表").click()
# 退出header-frame
driver.switch_to.default_content()
# 重新进入新的frame
driver.switch_to.frame("main-frame")
driver.find_element(By.NAME, "keyword").send_keys("abc996")
driver.find_element(By.XPATH, "//input[@type='submit']").click()
sleep(2)
driver.quit()
