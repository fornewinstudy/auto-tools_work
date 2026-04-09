from time import sleep
from selenium.webdriver.common.by import By
from PO.public.open import open_browser



def login(name="aaa",passwd='123456'):
    driver = open_browser()
    driver.find_element(By.NAME, "username").send_keys(name)
    driver.find_element(By.NAME, "password").send_keys(passwd)
    driver.find_element(By.NAME, "submit").click()
    sleep(0.5)
    return driver

if __name__ == '__main__':
    login()