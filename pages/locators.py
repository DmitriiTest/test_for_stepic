from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")

    PRISE_IN_PAGE = (By.CSS_SELECTOR, "p.price_color")
    NAME_OF_PRODUCT_IN_PAGE = (By.CSS_SELECTOR, ".product_main h1")
    ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
