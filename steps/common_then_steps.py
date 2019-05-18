from behave import then
from modules.pages.homepage import Homepage
from modules.pages.create_and_edit_page import CreateAndEditPage


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


@then('the user will be navigated back to the homepage')
def step_impl(context):
    page = Homepage(context.browser)
    assert page.isat_homepage(), "not at homepage"

@then('Delete computer cleanup')
def step_impl(context):
     page = Homepage(context.browser)
     page.search_for_computer(context.computer_name)
     page = CreateAndEditPage(context.browser)
     page.click_delete_computer()