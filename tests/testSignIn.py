import unittest
from selenium import webdriver

class OpenCartSignInTests(unittest.TestCase):

    def setUp(self):
        self.driver =webdriver.Chrome('drivers/chromedriver.exe')
        self.driver.maximize_window()
        self.driver.get('https://demo.opencart.com/')

    def test_sign_in_opencart(self):
        self.driver.find_element_by_class_name('dropdown')
        self.driver.find_element_by_xpath('//*[@id="top-links"]/ul/li[2]/ul/li[1]/a')

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':

    unittest.main()