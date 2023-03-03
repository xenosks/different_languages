import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait

class TestMainPage1():
    def test_check_button_add_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser.get(link)
        button = browser.find_elements(By.CSS_SELECTOR, "#add_to_basket_form > button")
        assert button, "Something is wrong"
