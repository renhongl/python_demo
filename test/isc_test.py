
import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class ISCTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()

    @classmethod
    def tearDownClass(self):
        self.driver.close()

    def test_login(self):
        """Should login successfully"""
        self.driver.get('http://168.63.251.253:9090/isc-sui/')
        time.sleep(3)
        account, password, *ign = self.driver.find_elements_by_css_selector('.form-item input')
        account.send_keys('sui-demo\\admin')
        password.send_keys('1q2w3e4r')
        self.driver.find_element_by_css_selector('.login-form-button').send_keys(Keys.ENTER)
        time.sleep(3)
        self.assertEqual('Application Library', self.driver.title)

    def test_title(self):
        """Title should be Application Library"""
        self.assertEqual('Application Library', self.driver.title)


    def test_go_to_address_mgmt(self):
        self.driver.get('http://168.63.251.253:9090/isc-sui/#/addressManagement')
        time.sleep(3)
        self.assertEqual('Address Management', self.driver.title)

    
    def test_show_graph(self):
        ...

if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='isc_test_dir'))