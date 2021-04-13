from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class ListPageItems:
    def __init__(self, driver):
        self.driver = driver
        self.input_sort = (By.ID, 'input-sort')

    def sort_by_price_high_low(self):

        input_sort_element = self.driver.find_element(*self.input_sort)
        input_sort = Select(input_sort_element)
        input_sort.select_by_visible_text('Price (High > Low)')


    def return_products_name_and_price(self):
        products = []
        price = []
        for i in range(3):
            product_name = self.driver.find_element_by_xpath(f'//*[@id="content"]/div[3]/div[{i + 1}]/div/div[2]/div[1]/h4/a').text
            products.append(product_name)
            product_price = self.driver.find_element_by_xpath(f'//*[@id="content"]/div[3]/div[{i + 1}]/div/div[2]/div[1]/p[2]').text
            price.append(product_price)

        print(products)
        print(price)

        return products, price