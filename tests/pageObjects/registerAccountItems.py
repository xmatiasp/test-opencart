from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class RegisterAccountItems:
    def __init__(self, driver):
        self.driver = driver
        self.first_name_input = (By.NAME, 'firstname')
        self.last_name_input = (By.NAME, 'lastname')
        self.email_input = (By.NAME, 'email')
        self.telephone_input = (By.NAME, 'telephone')
        self.password_input = (By.NAME, 'password')
        self.password_confirm_input = (By.NAME, 'confirm')
        self.suscribe_input = (By.NAME, 'newsletter')
        self.privacy_button = (By.NAME, 'agree')
        self.confirm_button = (By.XPATH, '//*[@id="content"]/form/div/div/input[2]')
        self.account_confirmation = (By.XPATH, '//*[@id="content"]/h1')
        self.account_registered = (By.XPATH, '//*[@id="account-register"]/div[1]')

    def fill_name_input(self, keys):
        self.driver.find_element(*self.first_name_input).send_keys(keys)

    def fill_last_name_input(self, keys):
        self.driver.find_element(*self.last_name_input).send_keys(keys)

    def fill_email_input(self, keys):
        self.driver.find_element(*self.email_input).send_keys(keys)

    def fill_telephone_input(self, keys):
        self.driver.find_element(*self.telephone_input).send_keys(keys)

    def fill_password_input(self, keys):
        self.driver.find_element(*self.password_input).send_keys(keys)

    def fill_confirm_password_input(self, keys):
        self.driver.find_element(*self.password_confirm_input).send_keys(keys)

    def click_suscribe_input(self):
        self.driver.find_element(*self.suscribe_input).click()

    def click_privacy_button(self):
        self.driver.find_element(*self.privacy_button).click()

    def click_confirm_button(self):
        self.driver.find_element(*self.confirm_button).click()

    def return_cofirmed_account_text(self):
        confirmed_account = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.account_confirmation))
        return confirmed_account.text

    def return_wrong_mail_account_text(self):
        wrong_mail = WebDriverWait(self.driver, 7).until(EC.presence_of_element_located(self.account_registered))
        return wrong_mail.text