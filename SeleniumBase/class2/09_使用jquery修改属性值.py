#!/usr/bin/env python3
# @Time : 2026/2/4 14:12
# @Author : 潘璐璐
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service("chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("http://www.mall.com/goods.php?id=16")
driver.maximize_window()
driver.implicitly_wait(10)
js = '$("#number").val(5)'  # 通过js修改页面元素的属性值
driver.execute_script(js)   # 执行js脚本，修改元素属性值
sleep(3)
driver.quit()
