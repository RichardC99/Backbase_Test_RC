from behave import given, when, then
from modules.pages.homepage import Homepage
from modules.pages.create_and_edit_page import CreateAndEditPage
from time import sleep


@given('A user has created a computer with known details for delete')
def step_impl(context):
    context.execute_steps('Given A user has navigated to the BB_Test_Webpage')
    page = Homepage(context.browser)
    if page.confirm_computer_present("BB_computer_for_edit_test"):
        context.computer_name = "BB_computer_for_edit_test"
        context.intro_date = "1986-04-04"
        context.discon_date = "2000-07-07"
        context.company = "Apple Inc."
        context.execute_steps('Given A user has navigated to the BB_Test_Webpage')

    else:
        context.execute_steps('Given A user has navigated to the BB_Test_Webpage')
        context.execute_steps('Given add a new computer is clicked')
        context.execute_steps('Given the User enters BB_computer_for_edit_test computer name')
        context.execute_steps('Given the user enters 1986-04-04 introduced date')
        context.execute_steps('Given the user enters 2000-07-07 discontinued date')
        context.execute_steps('Given the user selects Apple Inc. company')
        context.execute_steps('When the user clicks Save_this_computer')



@when('the Delete Computer button is clicked')
def step_impl(context):
    page = CreateAndEditPage(context.browser)
    page.click_delete_computer()


@then('the Computer is deleted from the table')
def step_impl(context):
    page = Homepage(context.browser)
    assert page.computer_deleted(), "computer not deleted"


@then('the computer will not have been added to the table')
def step_impl(context):
    page = Homepage(context.browser)
    page.search_for_computer(context.computer_name)
    assert page.computer_not_found(), "computer not deleted"




