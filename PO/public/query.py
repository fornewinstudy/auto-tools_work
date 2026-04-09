from PO.public.login import login
from selenium.webdriver.common.by import By
from time import sleep
import random

def Query(name="水果"):
    driver = login()
    driver.find_element(By.ID, "keyword").send_keys(name)
    driver.find_element(By.XPATH, "//*[@class='sea_submit']").click()
    sleep(0.5)
    # randoms = driver.find_elements(By.XPATH, '//*[@class="productimg"]/img')
    # random.choice(randoms).click()
    return driver

if __name__ == '__main__':
    Query()