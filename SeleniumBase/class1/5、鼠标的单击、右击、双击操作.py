from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains as ac


url = r"D:\python\pythonBase\SeleniumBase\Day1\test.html"
serv = Service("chromedriver.exe")
driver = webdriver.Chrome(service=serv)
driver.maximize_window()
driver.get(url)
driver.implicitly_wait(10)
# 使用鼠标左键点击某个元素可以直接使用click()，不需要使用鼠标事件
# 找到需要将鼠标单击的元素
e1 = driver.find_element(By.XPATH,'/html/body/form/input[3]')
# 调用鼠标事件，在e1元素上perform执行操作
ac(driver).click(e1).perform()
sleep(2)

# 定位需要双击的元素
e2 = driver.find_element(By.XPATH,'/html/body/form/input[2]')
ac(driver).double_click(e2).perform()
sleep(2)

# 定位需要右击的元素
e3 = driver.find_element(By.XPATH,'/html/body/form/input[4]')
ac(driver).context_click(e3).perform()
sleep(2)
driver.quit()



















