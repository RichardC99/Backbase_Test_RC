from behave import given, when, then
from modules.pages.createpage import CreatePage
from modules.pages.homepage import Homepage
from modules.helpers import AbstractJanitor
import config


# Givens
@given('the User enters {computer_name} computer name')
def step_impl(context, computer_name):
    page = CreatePage(context.browser)
    context.computer_name = computer_name
    name = computer_name.replace("null", "")
    page.enter_computer(name)
    # context.janitors.append(CleanUpAfterTest())


@given('the user enters {date} {format} date')
def step_impl(context, date, format):
    page = CreatePage(context.browser)

    if format == "introduced":
        context.intro_date = date
        date = date.replace("null", "")
        page.enter_intro_date(date)
    else:
        context.discon_date = date
        date = date.replace("null", "")
        page.enter_disc_date(date)


@given('the user selects {company} company')
def step_impl(context, company):
    context.company = company
    if company == "null":
       pass
    else:
        page = CreatePage(context.browser)
        page.select_company(company)


@when('the user clicks Save_this_computer')
def step_impl(context):
    page = CreatePage(context.browser)
    page.click_create()













# Thens

@then('the user will be navigated to "Create_Computer" page')
def step_impl(context):
    page = CreatePage(context.browser)
    assert page.isat_createpage(), "Not at ADD Computer page"


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
    page.enter_into_filter_by_name_input(name)
    page.click_filter_by_name_button()
    assert page.computer_has_correct_date(name, intro_date, "intro"), "date is incorrect"
    assert page.computer_has_correct_date(name, discon_date, "dison"), "date is incorrect"
    assert page.computer_has_correct_company(name, company)





# class CleanUpAfterTest(AbstractJanitor):
#     def __init__(self, cleanup):
#         self = self
#         self.CleanUp = cleanup
#
#     def clean_up(self):
#         page = Homepage(context.browser)
#         self.select_computer(context.computer_name)
#






