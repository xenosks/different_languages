import pytest as pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: '--language=en' or '--language=ru'")

@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    print("\nstart browser for test..")
    browser = webdriver.Chrome()

    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    yield browser
    # этот код выполнится после завершения теста
    print("\nquit browser..")
    browser.quit()