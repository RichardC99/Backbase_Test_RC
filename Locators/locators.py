from selenium.webdriver.common.by import By

class HomePageLocators():
    add_computer_button = (By.ID, "add")

    filter_by_name_button = (By.ID, "searchsubmit")

    filter_by_name_input = (By.ID, "searchbox")

    page_title = (By.XPATH, "/html/body/header/h1/a")

    computer_count = (By.XPATH, "//*[@id=\"main\"]/h1")


class CreatePageLocators:
    pass

class EditPageLocators:
    pass





