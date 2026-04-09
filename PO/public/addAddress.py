# from PO.public.addtocart import addtocart
from selenium.webdriver.common.by import By
from time import sleep
import random

def addAddress():
    # driver = addtocart()
    driver = driver.find_elements(By.XPATH, '//*[@name="province"]/option')
    driver.pop(0)
    random.choice(driver).click()
    sleep(1)
    driver1 = driver.find_elements(By.XPATH, '//*[@id="selCities_0"]/option')
    driver1.pop(0)
    random.choice(driver1).click()
    sleep(1)
    driver2 = driver.find_elements(By.XPATH, '//*[@id="selDistricts_0"]/option')
    driver2.pop(0)
    random.choice(driver2).click()
    driver.find_element(By.XPATH, '//*[@name="consignee"]').send_keys('张三')
    driver.find_element(By.XPATH, '//*[@id="address_0"]').send_keys('深圳龙岗坂田')
    driver.find_element(By.XPATH, '//*[@id="mobile_0"]').send_keys('13033453189')
    driver.find_element(By.XPATH, '//*[@class="btn"]').click()
    return driver

if __name__ == '__main__':
    addAddress()
