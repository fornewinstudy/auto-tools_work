#!/usr/bin/env python3
# @Time : 2026/2/4 11:38
# @Author : 潘璐璐
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

service = Service("chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get(r"D:\PythonProject\109\SeleniumBase\Day2\test.html")
driver.maximize_window()
driver.implicitly_wait(10)
# 如果只是鼠标左键点击某个元素可以直接使用click()，不需要使用鼠标事件
# 找到需要将鼠标单机的元素
e1 = driver.find_element(By.XPATH,"/html/body/form/input[3]")
# 调用鼠标事件，在e1元素上perform执行点击操作
ActionChains(driver).click(e1).perform()
sleep(2)

# 定位需要双击的元素
e2 = driver.find_element(By.XPATH,"/html/body/form/input[2]")
# 调用鼠标事件，在e2元素上perform执行双击操作
ActionChains(driver).double_click(e2).perform()
sleep(2)

# 定位需要右击的元素
e3 = driver.find_element(By.XPATH,"/html/body/form/input[4]")
# 调用鼠标事件，在e3元素上perform执行右击操作
ActionChains(driver).context_click(e3).perform()
sleep(2)
driver.quit()
