from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from modules.pages.basepage import Basepage
from Locators.locators import HomePageLocators, ComputerTableLocators
import pandas as pd
import datetime

import config

from time import sleep


class Homepage(Basepage):

    def goto_home_page(self):
        self.browser.get(self.base_url)

    def click_add_computer_button(self):
        self.click_element(*HomePageLocators.add_computer_button)

    def click_on_computer_name(self, name):
        self.click_element(By.LINK_TEXT, name)

    def click_filter_by_name_button(self):
        self.browser.find_element(*HomePageLocators.filter_by_name_button).click()

    def enter_into_filter_by_name_input(self, value):
        self.browser.find_element(*HomePageLocators.filter_by_name_input).send_keys(value)

    def computer_count(self):
        text = self.browser.find_element(*HomePageLocators.computer_count).text
        text = text.replace(" computers found", "")
        text = text.replace(",", "")
        return int(text)

    def computer_created(self, computer_name):

        text = self.find_element(*HomePageLocators.computer_created_message).text

        if text == f"Done! Computer {computer_name} has been created":
            return True
        else:
            return False

    def computer_deleted(self):
        text = self.find_element(*HomePageLocators.computer_deleted_message)
        if text == "Done! Computer has been deleted":
            return True
        else:
            return False

    def computer_has_correct_date(self, name, expected_date, date_column):

        if expected_date is "null":
            expected_date = expected_date.replace("null", "-")
        else:
            expected_date = datetime.datetime.strptime(expected_date, "%Y-%m-%d").strftime("%d %b %Y")
        if date_column == "intro":
            column = ComputerTableLocators.intro_date

        else:
            column = ComputerTableLocators.discon_date

        table = self.get_table_data()
        table_date = table.loc[name, column]

        if table_date == expected_date:
            return True
        else:
            return False

    def computer_has_correct_company(self, name, expected_company):
        column = ComputerTableLocators.company

        expected_company = expected_company.replace("null", "-")

        table = self.get_table_data()
        company = table.loc[name, column]

        if company == expected_company:
            return True
        else:
            return False











    def get_table_data(self):
        tbl = self.browser.find_element(*ComputerTableLocators.table).get_attribute('outerHTML')
        table = pd.read_html(tbl)
        table = table[0]
        table = table.set_index(ComputerTableLocators.computer_name, drop=False)
        return table






















