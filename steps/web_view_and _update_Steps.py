from behave import given, when, then
from modules.pages.create_and_edit_page import CreateAndEditPage
from modules.pages.homepage import Homepage


@given('A user has created a computer with known details and navigated to the edit screen')
def step_impl(context):
    context.execute_steps('Given A user has navigated to the BB_Test_Webpage')
    context.execute_steps('Given add a new computer is clicked')
    context.execute_steps('Given the User enters BB_computer_for_edit_test computer name')
    context.execute_steps('Given the user enters 1986-04-04 introduced date')
    context.execute_steps('Given the user enters 2000-07-07 discontinued date')
    context.execute_steps('Given the user selects Apple Inc. company')
    context.execute_steps('When the user clicks Save_this_computer')
    context.execute_steps('Given the User navigates to the Update Computer screen')


@then('the user will be navigated to "Edit_Computer" page')
def step_impl(context):
    page = CreateAndEditPage(context.browser)
    assert page.isat_Editpage(), "Not at add Edit page"
    page.click_cancel()


@then('the Computer will be updated')
def step_impl(context):
    page = Homepage(context.browser)
    assert page.computer_updated(context.computer_name), "Computer not updated"

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


@then('the number of computers found will stay the same')
def step_impl(context, n):
    page = Homepage(context.browser)
    no_computers = context.computer_count

    assert page.computer_count() == (no_computers), "computer count changed"