from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from .login_page import LoginPage
from selenium.common.exceptions import NoAlertPresentException # в начале файла
import math
import time

class BasketPage(BasePage):
    def should_not_item_in_basket(self):
        assert self.is_not_element_present(*MainPageLocators.NOT_ITEM_IN_BASKET), \
            "-------- ERROR!!! Item is presented, but should not be -----------"

    def should_be_text_basket_is_empty(self):
        assert self.is_element_present(*MainPageLocators.BASKET_IS_EMPTY), \
            "-------- ERROR!!! BASKET IS FULL -----------"
