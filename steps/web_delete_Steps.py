from behave import given, when, then
from modules.pages.createpage import CreatePage
from modules.pages.editpage import EditPage
from modules.pages.homepage import Homepage
from modules.helpers import AbstractJanitor


@given('A user has created a computer with known details')
def step_impl(context):
    context.execute_steps('Given A user has navigated to the BB_Test_Webpage')
    context.execute_steps('And add a new computer is clicked')
    context.execute_steps('Given the User enters <BB_Delete_computer_test> computer name')
    context.execute_steps('And the user enters <null> introduced date')
    context.execute_steps('And the user enters <null> discontinued date')
    context.execute_steps('And the user selects <null> company')
    context.execute_steps('When the user clicks Save_this_computer')


@given('the User navigates to the Update Computer screen')
def step_impl(context):
    page = Homepage(context.browser)
    page.click_on_computer_name(context.computer_name)


@when('the Delete Computer button is clicked')
def step_impl(context):
    page = EditPage(context.browser)
    page.click_delete_computer()

@then('the Computer is deleted from the table')
def step_impl():



