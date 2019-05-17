from behave import given, when, then
from modules.pages.homepage import Homepage
from modules.pages.create_and_edit_page import CreateAndEditPage



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
    context.computer_count = page.computer_count()
    page.enter_into_filter_by_name_input(context.computer_name)
    page.click_filter_by_name_button()
    page.click_on_computer_name(context.computer_name)


@then('the number of computers found will {incdec} by {n}')
def step_impl(context,incdec, n):
    page = Homepage(context.browser)

    if incdec == "decrease":
        n = -int(n)
        no_computers = context.computer_count
    else:
        n = int(n)
        no_computers = context.no_of_computers_start

    assert page.computer_count() == (no_computers + n), "computer count not changed"


@then('Delete computer cleanup')
def step_impl(context):
    page = Homepage(context.browser)
    page.click_on_computer_name(context.computer_name)
    page = CreateAndEditPage(context.browser)
    page.click_delete_computer()
