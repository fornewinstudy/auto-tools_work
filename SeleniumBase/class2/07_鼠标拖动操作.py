#!/usr/bin/env python3
# @Time : 2026/2/4 14:02
# @Author : 潘璐璐
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

service = Service("chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
driver.maximize_window()
driver.implicitly_wait(10)
# 获取需要拖动的元素位置
source = driver.find_element(By.ID,"dragger")
# 获取元素拖动的目标位置
target = driver.find_element(By.XPATH,"/html/body/div[3]")
# 调用鼠标事件，将source元素拖动到target元素的位置
ActionChains(driver).drag_and_drop(source,target).perform()
sleep(5)
driver.quit()
