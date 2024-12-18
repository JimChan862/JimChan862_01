#-*-coding:GBK -*-
#-*-coding:utf-8 -*-
# unitest + selenium �ٶ����� "�Ұ��й�" �Ĵ���

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class BaiduSearchTest(unittest.TestCase):
    """�ٶ����������࣬�̳���unittest.TestCase"""

    def setUp(self):
        """����ǰ��׼����������ʼ��Chrome���������"""
        self.driver = webdriver.Chrome()

    def test_search_wo_ai_zhongguo(self):
        """���԰ٶ��������ܣ�����'�Ұ��й�'����֤��������ùؼ���"""
        driver = self.driver
        driver.get("https://www.baidu.com")
        search_box = driver.find_element(By.ID, "kw")
        search_box.send_keys("�Ұ��й�")
        search_box.submit()
        time.sleep(2)
        self.assertIn("�Ұ��й�", driver.title)

    def tearDown(self):
        """���Խ���������������ر�Chrome���������"""
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()



#-*-coding:GBK -*-
#-*-coding:utf-8 -*-
# ��������Ŀ�
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class BaiduSearchTest(unittest.TestCase):
    """�ٶ����������࣬�̳���unittest.TestCase"""

    def setUp(self):
        """����ǰ��׼����������ʼ��Chrome���������"""
        self.driver = webdriver.Chrome()

    def test_search_wo_ai_zhongguo(self):
        """���԰ٶ��������ܣ�����'�Ұ��й�'����֤��������ùؼ���"""
        driver = self.driver
        driver.get("https://www.baidu.com")
        search_box = driver.find_element(By.ID, "kw")
        search_box.send_keys("�Ұ��й�")
        search_box.submit()
        time.sleep(2)
        self.assertIn("�Ұ��й�", driver.title)

    def test_search_empty(self):
        """����������Ϊ��ʱ�����"""
        driver = self.driver
        driver.get("https://www.baidu.com")
        search_box = driver.find_element(By.ID, "kw")
        search_box.send_keys("")
        search_box.submit()
        time.sleep(2)
        self.assertIn("�ٶ�һ��", driver.title)  # ��֤���ص��ٶ���ҳ

    def test_search_special_characters(self):
        """�������������ַ������"""
        driver = self.driver
        driver.get("https://www.baidu.com")
        search_box = driver.find_element(By.ID, "kw")
        search_box.send_keys("!@#$%^&*()")
        search_box.submit()
        time.sleep(2)
        # ��֤����������ܰ��������ַ�������
        self.assertIn("û���ҵ���ؽ��", driver.page_source)

    def test_search_non_existent_keyword(self):
        """�������������ڵĹؼ���"""
        driver = self.driver
        driver.get("https://www.baidu.com")
        search_box = driver.find_element(By.ID, "kw")
        search_box.send_keys("abcdefg12345")  # ����һ�������ڵĹؼ���
        search_box.submit()
        time.sleep(2)
        self.assertIn("û���ҵ���ؽ��", driver.page_source)

    def tearDown(self):
        """���Խ���������������ر�Chrome���������"""
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

