import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")

    parser.addoption('--language', action='store', default="en-gb",
                     help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    your_language = request.config.getoption("language")
#    your_language = None
#    browser = None
    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': your_language})
        browser = webdriver.Chrome(options=options)
        print("\n start chrome browser for test..")
    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", your_language)
        browser = webdriver.Firefox(firefox_profile=fp)
        print("\n start firefox browser for test..")
    else:
#        raise pytest.UsageError("--browser_name should be chrome or firefox")
        print('You do not input a nzme browser')
    yield browser
    print("\n quit browser..")
    browser.quit()