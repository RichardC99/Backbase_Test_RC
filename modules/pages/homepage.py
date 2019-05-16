from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from modules.pages.basepage import Basepage
from Locators.locators import HomePageLocators, ComputerTableLocators

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
        return int(text)

    def computer_created(self, computer_name):

        text = self.find_element(*HomePageLocators.computer_created_message).text

        if text == f"Done! Computer {computer_name} has been created":
            return True
        else:
            return False

    def table_has_correct_data(self, name, intro_date, discon_date, company ):
        table = ComputerTable(self.find_element(*ComputerTableLocators.table))
        all_data = table.all_data()
        print("all data")
        print(all_data)
        assert False




class ComputerTable(Basepage):
    def __init__(self, computer_table):
        self.table = computer_table

    def get_row_count(self):
        return len(self.table.find_elements(*ComputerTableLocators.rows)) -1

    def get_column_count(self):
        return len(self.table.find_elements(*ComputerTableLocators.columns))

    def row_data(self, computer_name):


        row = self.table.find_elements(By.LINK_TEXT, computer_name)
        rData = []
        for webElement in row:
            rData.append(webElement.text)

        return rData
    def all_data(self):
        no_of_rows = len(self.table.find_elements(*ComputerTableLocators.rows)) -1
        no_of_columns = len(self.table.find_elements(*ComputerTableLocators.columns))
        allData = []

        for i in range(2, no_of_rows):
            ro = []
            for j in range(1, no_of_columns):
                ro.append(self.table.find_element_by_xpath("//tr[" + str(i) + "]/td[" + str(j) + "]").text);

            allData.append(ro)

            print(allData)
            return allData






