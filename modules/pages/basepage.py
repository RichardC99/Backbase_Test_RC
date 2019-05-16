from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators.locators import HomePageLocators
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select

import config

from time import sleep


class Basepage():
    browser = None

    def __init__(self, browser):
        self.browser = browser
        self.base_url = config.url

    def click_element(self, *element):
        self.browser.find_element(*element).click()

    def enter_text(self, text, *element):
        self.browser.find_element(*element).send_keys(text)

    def find_element(self, *element):
       return self.browser.find_element(*element)

    def select_dropdown_by_text(self, value, *element):
        select = Select(self.browser.find_element(*element))
        select.select_by_visible_text(value)

    def page_loaded(self, *element):
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.visibility_of_element_located(*element))
        print("page loaded")




