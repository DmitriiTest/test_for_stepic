from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from .login_page import LoginPage
from selenium.common.exceptions import NoAlertPresentException # в начале файла
import math
import time


class ProductClass(BasePage):
    def add_product_in_basket(self):
        self.browser.get(self.url)
        price_in_page = self.browser.find_element(*MainPageLocators.PRISE_IN_PAGE).text
        name_of_product_in_page = self.browser.find_element(*MainPageLocators.NAME_OF_PRODUCT_IN_PAGE).text
        add_to_basket = self.browser.find_element(*MainPageLocators.ADD_TO_BASKET)
        add_to_basket.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def check_information(self):
        price_in_page = self.browser.find_element(*MainPageLocators.PRISE_IN_PAGE).text
#        name_of_product_in_page = self.browser.find_element(*MainPageLocators.NAME_OF_PRODUCT_IN_PAGE).text
#        print (price_in_page, '111111111111111111111111111')

        price_in_basket = self.browser.find_element_by_xpath('//*[@id="messages"]/div[3]/div/p[1]/strong').text
        print(price_in_basket, 'your price in basket')

        product_in_basket = self.browser.find_element_by_xpath('//*[@id="messages"]/div[1]/div/strong').text
        print(product_in_basket, 'your product in basket')
        name_of_product_in_page = self.browser.find_element(*MainPageLocators.NAME_OF_PRODUCT_IN_PAGE).text

        assert product_in_basket == name_of_product_in_page, 'ERROR, name product in page not equal product in basket'
        assert price_in_page == price_in_basket, 'ERROR, price in page not equal price in basket'
