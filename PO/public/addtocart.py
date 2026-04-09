from PO.public.query import Query
from selenium.webdriver.common.by import By
from time import sleep
import random

def addtocart():
    add = Query()
    randoms = add.find_elements(By.XPATH, '//*[@class="productimg"]/img')
    random.choice(randoms).click()
    headles = add.window_handles  # 获取全部窗口
    add.switch_to.window(headles[-1])
    add.find_element(By.XPATH, '//*[@id="buy_btn"]').click()
    # time.sleep(1)
    add.find_element(By.XPATH, '//*[@class="go"]/a[2]').click()
    add.find_element(By.XPATH, '//*[@class="btn"]').click()
    return add
if __name__ == '__main__':
    addtocart()




