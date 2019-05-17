from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from modules.pages.basepage import Basepage
from Locators.locators import EditPageLocators
import config

from time import sleep


class EditPage(Basepage):

    def click_delete_computer(self):
        self.click_element(*EditPageLocators.delete_computer_button)
