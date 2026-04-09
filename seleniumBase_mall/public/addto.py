from PO.public.login import login
from selenium.webdriver.common.by import By
import random
from time import sleep

def addtocart(name="张三",add="深圳龙岗",):
    add = login()
    add.find_element(By.XPATH,'//*[@id="userinfo-bar"]/li[1]/a').click()
    add.find_element(By.XPATH,'//*[@id="wrapper"]/div[2]/div[1]/ul/li[1]/ul/li/a[2]').click()
    driver = add.find_elements(By.XPATH,'//*[@id="selProvinces_0"]/option')
    driver.pop(0)
    random.choice(driver).click()
    sleep(0.5)
    driver1 = add.find_elements(By.XPATH,'//*[@id="selCities_0"]/option')
    driver1.pop(0)
    random.choice(driver1).click()
    sleep(0.5)
    driver2 = add.find_elements(By.XPATH,'//*[@id="selDistricts_0"]/option')
    driver2.pop(0)
    random.choice(driver2).click()
    add.find_element(By.XPATH,'//*[@id="consignee_0"]').send_keys('')
    return add
if __name__ == '__main__':
    addtocart()
