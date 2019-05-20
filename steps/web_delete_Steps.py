from behave import given, when, then
from modules.pages.homepage import Homepage
from modules.pages.create_and_edit_page import CreateAndEditPage
from time import sleep


@given('A user has created a computer with known details for deletion')
def step_impl(context):
    context.execute_steps('Given A user has navigated to the BB_Test_Webpage')
    computer_name = "BB_computer_for_delete_testcls"
    page = Homepage(context.browser)
    page2 = CreateAndEditPage(context.browser)
    while page.confirm_computer_present(computer_name):
        page.click_on_computer_name(computer_name)
        page2.click_delete_computer()
        if not (page.confirm_computer_present(computer_name)):
            break

    context.execute_steps('Given add a new computer is clicked')
    context.execute_steps('Given the User enters BB_computer_for_delete_test computer name')
    context.execute_steps('Given the user enters 1986-04-04 introduced date')
    context.execute_steps('Given the user enters 2000-07-07 discontinued date')
    context.execute_steps('Given the user selects Apple Inc. company')
    context.execute_steps('When the user clicks Save_this_computer')


@given('A user has created a computer with known details for API deletion')
def step_impl(context):
    context.execute_steps('Given A user has navigated to the BB_Test_Webpage')
    computer_name = "BB_computer_for_delete_testcls"
    page = Homepage(context.browser)
    page2 = CreateAndEditPage(context.browser)
    while page.confirm_computer_present(computer_name):
        page.click_on_computer_name(computer_name)
        page2.click_delete_computer()
        if not (page.confirm_computer_present(computer_name)):
            break

    context.execute_steps('Given add a new computer is clicked')
    context.execute_steps('Given the User enters BB_computer_for_delete_test computer name')
    context.execute_steps('Given the user enters 1986-04-04 introduced date')
    context.execute_steps('Given the user enters 2000-07-07 discontinued date')
    context.execute_steps('Given the user selects Apple Inc. company')
    context.execute_steps('When the user clicks Save_this_computer')
    context.execute_steps('the User navigates to the Update Computer screen')



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




