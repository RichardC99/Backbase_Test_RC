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

    def isat_createpage(self):
        # self.wait_for_element(*CreatePageLocators.add_computer_title)
        text = self.find_element(*CreatePageLocators.add_computer_title).text
        print(text)

        if text == "Add a computer":
            return True
        else:
            return False


