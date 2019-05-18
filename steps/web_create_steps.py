from behave import given, then
from modules.pages.create_and_edit_page import CreateAndEditPage
from modules.pages.homepage import Homepage
from modules.helpers import AbstractJanitor


@given('the User navigates to the Update Computer screen')
def step_impl(context):
    page = Homepage(context.browser)
    context.computer_count = page.computer_count()
    page.search_for_computer(context.computer_name)
    page.click_on_computer_name(context.computer_name)


@given('the User enters {computer_name} computer name')
def step_impl(context, computer_name):
    context.page = CreateAndEditPage(context.browser)
    context.computer_name = computer_name
    if computer_name != "null":
        context.page.enter_computer(computer_name)
    else:
        pass


@given('the user enters {date} {format} date')
def step_impl(context, date, format):
    page = CreateAndEditPage(context.browser)
    if format == "introduced":
            context.intro_date = date
            if date != "null":
                page.enter_intro_date(date)
            else:
                pass
    elif format == "discontinued":
            context.discon_date = date
            if date != "null":
                page.enter_disc_date(date)
            else:
                pass


@then('the user will be navigated to "Create_Computer" page')
def step_impl(context):
    page = CreateAndEditPage(context.browser)
    assert page.isat_Createpage(), "Not at add Computer page"


@then('the user will remain at the add computer screen')
def step_impl(context):
    page = CreateAndEditPage(context.browser)
    assert page.isat_Createpage(), "Not at add computer page"


@then('the Computer will be created')
def step_impl(context):
    page = Homepage(context.browser)
    assert page.computer_created(context.computer_name), "Computer not created"


@then('the computer has been added to the table with the correct information')
def step_impl(context):
    name = context.computer_name
    intro_date = context.intro_date
    discon_date = context.discon_date
    company = context.company

    page = Homepage(context.browser)
    page.search_for_computer(name)
    assert page.computer_has_correct_date(name, intro_date, "intro"), "intro_date is incorrect"
    assert page.computer_has_correct_date(name, discon_date, "dison"), "discon_date is incorrect"
    assert page.computer_has_correct_company(name, company)
    

@then('the correct error message will appear {error}')
def step_impl(context, error):
    page = CreateAndEditPage(context.browser)
    if error == "name_required":
        assert page.invalid_name_error(), "error message not present"

    elif error == "invalid_intro_date_format":
        assert page.invalid_intro_date_format(), "error message not present"

    elif error == "invalid_discon_date_format":
        assert page.invalid_discon_date_format(), "error message not present"

    elif error == "all_data_invalid":
        assert page.invalid_name_error(), "error message not present"
        assert page.invalid_intro_date_format(), "error message not present"
        assert page.invalid_discon_date_format(), "error message not present"




# class CleanUpAfterTest(AbstractJanitor):
#     def __init__(self, computer_name, browser):
#
#         self.computer_name = computer_name
#         self.browser = browser
#     def clean_up(self):
#         self.page = Homepage(self.browser)
#         self.page.search_for_computer(self.computer_name)
#         self.page.click_on_computer_name(self.computer_name)
#         self.page = CreateAndEditPage(self.browser)
#         self.page.click_delete_computer()
#








