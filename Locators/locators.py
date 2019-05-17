from selenium.webdriver.common.by import By


class HomePageLocators():
    add_computer_button = (By.ID, "add")

    filter_by_name_button = (By.ID, "searchsubmit")

    filter_by_name_input = (By.ID, "searchbox")

    page_title = (By.XPATH, "/html/body/header/h1/a")

    computer_count = (By.XPATH, "//*[@id=\"main\"]/h1")

    computer_created_message = (By.XPATH, "//*[@id=\"main\"]/div[1]")

    computer_deleted_message = (By.XPATH, "//*[@id=\"main\"]/div[1]")

    nothing_to_display = (By.CSS_SELECTOR, "#main > div.well > em")

class ComputerTableLocators():

    table = (By.XPATH, "//*[@id=\"main\"]/table")

    computer_name = "Computer name"

    intro_date = "Introduced"

    discon_date = "Discontinued"

    company = "Company"



class CreateAndEditPageLocators:
    add_computer_title = (By.XPATH, "//*[@id=\"main\"]/h1")

    computer_name_input = (By.ID, "name")

    introduced_date = (By.ID, "introduced")

    discontinued_date =(By.ID, "discontinued")

    company_dropdown = (By.ID, "company")

    create_computer = (By.XPATH, "//*[@id=\"main\"]/form/div/input")

    delete_computer_button = (By.XPATH, "//*[@id=\"main\"]/form[2]/input")

    Edit_computer_title = (By.XPATH, "//*[@id=\"main\"]/h1")

    computer_name_required = (By.XPATH, "//*[@id=\"main\"]/form/fieldset/div[1]")

    invalid_intro_date = (By.XPATH, "//*[@id=\"main\"]/form/fieldset/div[2]")

    invalid_dscon_date = (By.XPATH, "//*[@id=\"main\"]/form/fieldset/div[3]")






