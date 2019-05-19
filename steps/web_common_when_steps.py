from behave import when
from modules.pages.create_and_edit_page import CreateAndEditPage


@when('the user clicks cancel')
def step_impl(context):
    page = CreateAndEditPage(context.browser)
    page.click_cancel()
