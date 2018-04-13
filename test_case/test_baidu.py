# @Author: cherong 
# @Date: 2018-04-12 16:03:09 
# @Last Modified by:   cherong 
# @Last Modified time: 2018-04-12 16:03:09 


from selenium import webdriver
import unittest
import time


class Baidu(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_ulr = "http://www.baidu.com/"
    def test_baidu_serach(self):
        driver = self.driver
        driver.get(self.base_ulr)
        driver.find_element_by_id("kw").send_keys("zeijibafan")
        driver.find_element_by_id("su").click

    def tearDown(self):
        self.driver.quit


if __name__ == "__main__":
    unittest.main()