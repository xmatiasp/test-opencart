from selenium.webdriver.common.by import By

class HomePageItems:
    def __init__(self, driver):
        self.driver = driver
        self.my_account_button = (By.XPATH, '//*[@id="top-links"]/ul/li[2]/a/span[1]')
        self.register_button = (By.XPATH, '//*[@id="top-links"]/ul/li[2]/ul/li[1]/a')

    def click_in_myaccount(self):
        self.driver.find_element(*self.my_account_button).click()

    def click_in_register(self):
        self.driver.find_element(*self.register_button).click()