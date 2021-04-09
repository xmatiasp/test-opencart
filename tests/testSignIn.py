import unittest
from selenium import webdriver
from tests.pageObjects.homePageItems import HomePageItems
from tests.pageObjects.registerAccountItems import RegisterAccountItems
import time

class OpenCartSignInTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('drivers/chromedriver.exe')
        self.driver.maximize_window()
        self.driver.get('https://demo.opencart.com/')
        self.itemsHomePage = HomePageItems(self.driver)
        self.itemsRegisterAcc = RegisterAccountItems(self.driver)

    def test_register_in_opencart_(self):
        self.itemsHomePage.click_in_myaccount()
        self.itemsHomePage.click_in_register()
        self.itemsRegisterAcc.fill_name_input('Bruce')
        self.itemsRegisterAcc.fill_last_name_input('Wayne')
        #utilizar nuevo mail cada vez que se corra esta prueba
        self.itemsRegisterAcc.fill_email_input('batman9@prueba.com')
        self.itemsRegisterAcc.fill_telephone_input('1234666')
        self.itemsRegisterAcc.fill_password_input('123prueba')
        self.itemsRegisterAcc.fill_confirm_password_input('123prueba')
        self.itemsRegisterAcc.click_suscribe_input()
        self.itemsRegisterAcc.click_privacy_button()
        self.itemsRegisterAcc.click_confirm_button()
        self.assertEqual('Your Account Has Been Created!', self.itemsRegisterAcc.return_cofirmed_account_text())

    def test_register_in_opencart_with_account_registered(self):
        self.itemsHomePage.click_in_myaccount()
        self.itemsHomePage.click_in_register()
        self.itemsRegisterAcc.fill_name_input('Bruce')
        self.itemsRegisterAcc.fill_last_name_input('Wayne')
        self.itemsRegisterAcc.fill_email_input('batman1@prueba.com')
        self.itemsRegisterAcc.fill_telephone_input('1234666')
        self.itemsRegisterAcc.fill_password_input('123prueba')
        self.itemsRegisterAcc.fill_confirm_password_input('123prueba')
        self.itemsRegisterAcc.click_suscribe_input()
        self.itemsRegisterAcc.click_privacy_button()
        self.itemsRegisterAcc.click_confirm_button()
        self.assertEqual('Warning: E-Mail Address is already registered!', self.itemsRegisterAcc.return_wrong_mail_account_text())


    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()