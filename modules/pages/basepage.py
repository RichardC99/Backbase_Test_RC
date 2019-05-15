from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select

import config

from time import sleep


class Basepage:
    browser = None

    def __init__(self, browser):
        self.browser = browser
        self.base_url = config.url

