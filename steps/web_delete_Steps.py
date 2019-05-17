from behave import given, when, then
from modules.pages.editpage import EditPage
from modules.pages.homepage import Homepage
from time import sleep


@given('A user has created a computer with known details')
def step_impl(context):
    context.execute_steps('Given A user has navigated to the BB_Test_Webpage')
    context.execute_steps('And add a new computer is clicked')
    context.execute_steps('Given the User enters <BB_Delete_computer_test> computer name')
    context.execute_steps('And the user enters <null> introduced date')
    context.execute_steps('And the user enters <null> discontinued date')
    context.execute_steps('And the user selects <null> company')
    sleep(5)
    context.execute_steps('When the user clicks Save_this_computer')


@when('the Delete Computer button is clicked')
def step_impl(context):
    page = EditPage(context.browser)
    page.click_delete_computer()
    sleep(5)


@then('the Computer is deleted from the table')
def step_impl(context):
    page = Homepage(context.browser)
    assert page.computer_deleted(), "computer not deleted"


@then('the computer will not be able to be found')
def step_impl(context):
    page = Homepage(context.browser)
    page.enter_into_filter_by_name_input(context.computer_name)
    page.click_filter_by_name_button()
    assert page.computer_not_found(), "computer not deleted"


