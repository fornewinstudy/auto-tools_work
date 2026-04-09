from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


url = r"http://www.mall.com/goods.php?id=16"
serv = Service("chromedriver.exe")
driver = webdriver.Chrome(service=serv)
driver.maximize_window()
driver.get(url)
driver.implicitly_wait(10)

js = "$('#number').val(5)" # 通过js修改页面元素的属性值
driver.execute_script(js)  #通过执行js脚本，修改元素属性值
sleep(3)
driver.quit()


















