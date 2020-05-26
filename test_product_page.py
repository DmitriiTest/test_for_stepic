from .pages.main_page import MainPage
from .pages.login_page import LoginPage
import time
from .pages.product_page import ProductClass
import math


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                          # открываем страницу
    z = ProductClass(browser, link)
    z.add_product_in_basket()
    start_quiz = ProductClass(browser, link)
    start_quiz.solve_quiz_and_get_code()
    check_info = ProductClass(browser, link)
    check_info.check_information()
