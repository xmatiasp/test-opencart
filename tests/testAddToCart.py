import time
import unittest
from selenium import webdriver
from tests.pageObjects.homePageItems import HomePageItems
from tests.pageObjects.listPageItems import ListPageItems

class AddToCartTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('drivers/chromedriver.exe')
        self.driver.maximize_window()
        self.driver.get('https://demo.opencart.com/')
        self.itemsHomePage = HomePageItems(self.driver)
        self.itemsListPage = ListPageItems(self.driver)

    def test_add_macbook_in_cart(self):
        self.itemsHomePage.search_product('MacBook')
        self.itemsListPage.sort_by_price_high_low()
        time.sleep(3)
        self.itemsListPage.return_products_name_and_price()


    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()