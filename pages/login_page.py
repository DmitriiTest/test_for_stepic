from .base_page import BasePage
from .locators import LoginPageLocators
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        x = self.browser.current_url
        assert "login" in x, "E R R O R, url don't has str - login"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "E R R O R, LOGIN FORM is not presented"


    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "E R R O R, REGISTRATION FORM is not presented"

    def register_new_user(self, email, password):
        input_email = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        input_email.send_keys(email)
        input_password = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD)
        input_password.send_keys(password)
        agree_password = self.browser.find_element(*LoginPageLocators.ACCEPT_PASSWORD_FIELD)
        agree_password.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()
