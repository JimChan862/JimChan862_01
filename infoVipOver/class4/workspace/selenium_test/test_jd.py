import time

from selenium import webdriver

def test_baidu():
    driver=webdriver.Chrome()
    driver.get('http://www.jd.com')
    time.sleep(3)
    driver.quit()