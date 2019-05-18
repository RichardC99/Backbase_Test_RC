from behave import when
from modules.pages.create_and_edit_page import CreateAndEditPage


@when('the user clicks Save_this_computer')
def step_impl(context):
    page = CreateAndEditPage(context.browser)
    page.click_Create()
    # context.janitors.append(CleanUpAfterTest(context.computer_name, context.browser))


@when('the user clicks cancel')
def step_impl(context):
    page = CreateAndEditPage(context.browser)
    page.click_cancel()