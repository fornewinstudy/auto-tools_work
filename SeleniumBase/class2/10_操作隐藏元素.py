#!/usr/bin/env python3
# @Time : 2026/2/4 14:16
# @Author : 潘璐璐
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get(r"D:\PythonProject\109\SeleniumBase\Day2\Hidden.html")
driver.maximize_window()
driver.implicitly_wait(10)
# 返回False表示元素被隐藏，无法直接定位操作
print(driver.find_element(By.ID, "username").is_displayed())
# 通过js修改页面的元素属性值
js = 'document.getElementById("username").style="block"'
driver.execute_script(js)   # 执行js操作，修改页面元素属性值
driver.find_element(By.ID,"username").send_keys("张三")
sleep(2)
driver.quit()
