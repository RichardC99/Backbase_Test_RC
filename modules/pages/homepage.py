from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from modules.pages.Helpers import Helpers
from Locators.locators import HomePageLocators
import config

from time import sleep


class Homepage(Helpers):

    def goto(self):
        self.browser.get(self.base_url)

    def add_computer_button(self):
        self.browser.find_element(*HomePageLocators.add_computer_button).click()

    def filter_by_name_button(self):
        self.browser.find_element(*HomePageLocators.filter_by_name_button).click()

    def filter_by_name_input(self, value):
        self.browser.find_element(*HomePageLocators.filter_by_name_input).send_keys(value)

    def page_title(self):
        self.browser.find_element(*HomePageLocators.page_title)

    def computer_count(self):
        self.browser.find_element(HomePageLocators.computer_count)





