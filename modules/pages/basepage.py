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

    def wait_for_element(self, *element):

        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(*element)
        )

    def click_element(self, *element):
        self.browser.find_element(*element).click()


    def find_element(self, *element):

        return self.browser.find_element(*element)


