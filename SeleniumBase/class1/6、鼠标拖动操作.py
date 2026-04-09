from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains as ac


url = r"http://sahitest.com/demo/dragDropMooTools.htm"
serv = Service("chromedriver.exe")
driver = webdriver.Chrome(service=serv)
driver.maximize_window()
driver.get(url)
driver.implicitly_wait(10)
# 获取需要拖动元素的位置
source = driver.find_element(By.ID,'dragger')
# 获取元素拖动的目标位置
target = driver.find_element(By.XPATH,'/html/body/div[4]')
# 调用鼠标事件，将source元素拖动到target元素的位置
ac(driver).drag_and_drop(source,target).perform()
sleep(2)
driver.quit()

















