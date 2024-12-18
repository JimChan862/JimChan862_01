#-*-coding:GBK -*-
#-*-coding:utf-8 -*-
# unitest + selenium 百度搜索 "我爱中国" 的代码

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class BaiduSearchTest(unittest.TestCase):
    """百度搜索测试类，继承自unittest.TestCase"""

    def setUp(self):
        """测试前的准备工作，初始化Chrome浏览器驱动"""
        self.driver = webdriver.Chrome()

    def test_search_wo_ai_zhongguo(self):
        """测试百度搜索功能，搜索'我爱中国'并验证标题包含该关键词"""
        driver = self.driver
        driver.get("https://www.baidu.com")
        search_box = driver.find_element(By.ID, "kw")
        search_box.send_keys("我爱中国")
        search_box.submit()
        time.sleep(2)
        self.assertIn("我爱中国", driver.title)

    def tearDown(self):
        """测试结束后的清理工作，关闭Chrome浏览器驱动"""
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()



#-*-coding:GBK -*-
#-*-coding:utf-8 -*-
# 导入所需的库
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class BaiduSearchTest(unittest.TestCase):
    """百度搜索测试类，继承自unittest.TestCase"""

    def setUp(self):
        """测试前的准备工作，初始化Chrome浏览器驱动"""
        self.driver = webdriver.Chrome()

    def test_search_wo_ai_zhongguo(self):
        """测试百度搜索功能，搜索'我爱中国'并验证标题包含该关键词"""
        driver = self.driver
        driver.get("https://www.baidu.com")
        search_box = driver.find_element(By.ID, "kw")
        search_box.send_keys("我爱中国")
        search_box.submit()
        time.sleep(2)
        self.assertIn("我爱中国", driver.title)

    def test_search_empty(self):
        """测试搜索框为空时的情况"""
        driver = self.driver
        driver.get("https://www.baidu.com")
        search_box = driver.find_element(By.ID, "kw")
        search_box.send_keys("")
        search_box.submit()
        time.sleep(2)
        self.assertIn("百度一下", driver.title)  # 验证返回到百度首页

    def test_search_special_characters(self):
        """测试搜索特殊字符的情况"""
        driver = self.driver
        driver.get("https://www.baidu.com")
        search_box = driver.find_element(By.ID, "kw")
        search_box.send_keys("!@#$%^&*()")
        search_box.submit()
        time.sleep(2)
        # 验证搜索结果可能包含特殊字符的描述
        self.assertIn("没有找到相关结果", driver.page_source)

    def test_search_non_existent_keyword(self):
        """测试搜索不存在的关键词"""
        driver = self.driver
        driver.get("https://www.baidu.com")
        search_box = driver.find_element(By.ID, "kw")
        search_box.send_keys("abcdefg12345")  # 输入一个不存在的关键词
        search_box.submit()
        time.sleep(2)
        self.assertIn("没有找到相关结果", driver.page_source)

    def tearDown(self):
        """测试结束后的清理工作，关闭Chrome浏览器驱动"""
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

