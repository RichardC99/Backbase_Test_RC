from behave import given, when, then
from modules.pages.homepage import Homepage


@given('A user has navigated to the BB_Test_Webpage')
def step_impl(context):
    page = Homepage(context.browser)
    page.goto_home_page()
    context.no_of_computers_start = page.computer_count()


@given('add a new computer is clicked')
def step_impl(context):
    page = Homepage(context.browser)
    page.click_add_computer_button()


@given('the User navigates to the Update Computer screen')
def step_impl(context):
    page = Homepage(context.browser)
    page.click_on_computer_name(context.computer_name)


@then('the number of computers found will increase by {n}')
def step_impl(context, n):
    page = Homepage(context.browser)
    assert page.computer_count() == (context.no_of_computers_start+int(n)), "computer count not increased"