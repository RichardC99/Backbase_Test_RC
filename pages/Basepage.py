from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
import config

from time import sleep

class Basepage():
    browser = None

    def __init__(self, browser):
        self.browser = browser
        self.base_url = config.url

    def add_computer_button(self):
        self.browser.find_element_by_id("add").click()

    def filter_by_name_button(self):
        self.browser.find_element_by_id("searchsubmit").click()

    def filter_by_name_input(self, value):
        self.browser.find_element_by_id("searchbox").send_keys(value)

  