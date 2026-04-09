from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

url = r"http://www.mall.com/goods.php?id=16"
serv = Service("chromedriver.exe")
driver = webdriver.Chrome(service=serv)
driver.maximize_window()
driver.get(url)
driver.implicitly_wait(10)
# 前端对于某个个别元素会有一个焦点，如果直接清空购物车数量，会让元素失去焦点，从而页面弹出告警框
# 如果直接使用send_keys()，会在原有的数字后面加上字符，并不是用户想要购买的真实数量
driver.find_element(By.ID,'number').send_keys(Keys.BACKSPACE)
driver.find_element(By.ID,'number').send_keys("5")
sleep(2)
driver.quit()



















