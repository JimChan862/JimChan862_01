from selenium import webdriver
import time

class BasePage:
    """
    基础page层，封装一些常用方法。
    """

    def __init__(self, driver):
        # 导入一下 webdriver包,方便后面代码编写，写完注释掉
        # self.driver = webdriver.Chrome()
        self.driver = driver

    # 打开页面
    def open(self, url=None):
        if url is None:
            self.driver.get(self.url)
        else:
            self.driver.get(url)

    # 元素定位
    def locator(self, name,value):
        return self.driver.find_element(name, value)


    # 获取title，获取网页标题栏
    def get_title(self):
        return self.driver.title

    # 获取页面text，获取页面文本，使用xpath定位
    def get_text(self, path):
        return self.locator("xpath",path).text

    # 执行JavaScript脚本
    def js(self, script):
        self.driver.execute_script(script)

    # 休眠时间
    def sleep(self, sec):
        time.sleep(sec)
