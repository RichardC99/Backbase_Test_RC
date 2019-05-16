from behave import given, when, then
from modules.pages.createpage import CreatePage
import config

@then('the user will be navigated to "Create_Computer" page')
def step_impl(context):
    page = CreatePage(context.browser)
    assert page.isat_createpage(), "Not at ADD Computer page"
