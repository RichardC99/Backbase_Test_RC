from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from modules.pages.basepage import Basepage
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select

class Helpers(Basepage):

    def wait_for_element(self, element):
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(element)
        )

    def click_element(self, element):
        element.click()