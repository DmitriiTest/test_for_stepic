from .base_page import BasePage
from .locators import MainPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        x = self.browser.current_url
        assert "login" in x, "E R R O R, url don't has str - login"

    def should_be_login_form(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_FORM), "E R R O R, LOGIN FORM is not presented"


    def should_be_register_form(self):
        assert self.is_element_present(*MainPageLocators.REGISTRATION_FORM), "E R R O R, REGISTRATION FORM is not presented"
