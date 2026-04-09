from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from PO.conf.config import login_url,chrome


def open_browser():
    url = login_url
    serv = Service(chrome)
    driver = webdriver.Chrome(service=serv)
    driver.maximize_window()
    driver.get(url)
    driver.implicitly_wait(10)
    return driver


if __name__ == '__main__':
    open_browser()