from behave import given, when, then
from modules.pages.createpage import CreatePage
import config


# Givens
@given('the User enters <Computer_name> computer name')
def step_impl(context):
    pass

@given('the user enters <Introduced_Date> introduced date')
def step_impl(context):
    pass

@given('the user enters <Discontinued_Date> discontinued date')
def step_impl(context):
    pass

@given('the user selects <Company> company')
def step_impl(context):
    pass











# Thens

@then('the user will be navigated to "Create_Computer" page')
def step_impl(context):
    page = CreatePage(context.browser)
    assert page.isat_createpage(), "Not at ADD Computer page"









