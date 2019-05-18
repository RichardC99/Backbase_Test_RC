from behave import given, when, then
from modules.pages.create_and_edit_page import CreateAndEditPage
from modules.pages.homepage import Homepage
import config


@then('the user will be navigated to "Create_Computer" page')
def step_impl(context):
    page = CreateAndEditPage(context.browser)
    assert page.isat_Editpage(), "Not at add Edit page"


@then('the Computer will be updated')
def step_impl(context):
    page = Homepage(context.browser)
    assert page.computer_created(context.computer_name), "Computer not updated"

@then('the computer is updated on the table with the correct information')
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