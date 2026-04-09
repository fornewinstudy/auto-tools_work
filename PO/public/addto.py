from PO.public.login import login
from selenium.webdriver.common.by import By
import random
from time import sleep

def addto(name="张三",address="深圳龙岗",EM="aaa@qq.com",number="13033453189"):
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
    add.find_element(By.XPATH,'//*[@id="consignee_0"]').send_keys(name)
    add.find_element(By.XPATH,'//*[@id="address_0"]').send_keys(address)
    add.find_element(By.XPATH,'//*[@id="email_0"]').send_keys(EM)
    add.find_element(By.XPATH,'//*[@id="mobile_0"]').send_keys(number)
    add.find_element(By.XPATH,'//*[@align="center"]/input[1]').click()
    return add
if __name__ == '__main__':
    addto()
