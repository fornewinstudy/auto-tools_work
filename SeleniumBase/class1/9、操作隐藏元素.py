from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


url = r"D:\python\pythonBase\SeleniumBase\Day1\Hidden.html"
serv = Service("chromedriver.exe")
driver = webdriver.Chrome(service=serv)
driver.maximize_window()
driver.get(url)
driver.implicitly_wait(10)
print(driver.find_element(By.ID,'username').is_enabled())
js = 'document.getElementById("username").style="block"'
driver.execute_script(js)
driver.find_element(By.ID,'username').send_keys('张三')
sleep(2)
driver.quit()
















