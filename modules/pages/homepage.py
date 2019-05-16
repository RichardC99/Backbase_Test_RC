from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from modules.pages.basepage import Basepage
from Locators.locators import HomePageLocators
import config

from time import sleep


class Homepage(Basepage):

    def goto_home_page(self):
        self.browser.get(self.base_url)

    def click_add_computer_button(self):
        self.click_element(*HomePageLocators.add_computer_button)

    def click_filter_by_name_button(self):
        self.browser.find_element(*HomePageLocators.filter_by_name_button).click()

    def enter_into_filter_by_name_input(self, value):
        self.browser.find_element(*HomePageLocators.filter_by_name_input).send_keys(value)

    def computer_count(self):
        text = self.browser.find_element(*HomePageLocators.computer_count).text
        text = text.replace(" computers found", "")
        text = text.replace(",", "")
        print(text)

    def computer_created(self, computer_name):

        text = self.find_element(*HomePageLocators.computer_created_message).text

        if text == f"Done! Computer {computer_name} has been created":
            return True
        else:
            return False






