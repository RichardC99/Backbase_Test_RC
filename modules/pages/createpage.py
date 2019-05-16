from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from modules.pages.basepage import Basepage
from Locators.locators import CreatePageLocators
import config

from time import sleep

class CreatePage(Basepage):

    def enter_computer(self, name):

        self.enter_text(name, *CreatePageLocators.computer_name_input)

    def enter_intro_date(self, date):
        self.enter_text(date, *CreatePageLocators.introduced_date)

    def enter_disc_date(self, date):
        self.enter_text(date, *CreatePageLocators.discontinued_date)

    def select_company(self, company):
        self.select_dropdown_by_text(company, *CreatePageLocators.company_dropdown)

    def click_create(self):
        self.click_element(*CreatePageLocators.create_computer)

















    def isat_createpage(self):
        # self.wait_for_element(*CreatePageLocators.add_computer_title)
        text = self.find_element(*CreatePageLocators.add_computer_title).text
        print(text)

        if text == "Add a computer":
            return True
        else:
            return False


