from behave import given, when, then
from modules.pages.createpage import CreatePage
import config


# Givens
@given('the User enters {Computer_name} computer name')
def step_impl(context, computer_name):
    page = CreatePage(context.browser)
    name = computer_name.replace("null", "")
    page.enter_computer(name)


@given('the user enters {date} {format} date')
def step_impl(context, date, format):
    page = CreatePage(context.browser)
    date = date.replace("null", "")

    if format == "introduced":
        context.intro_date = date
        page.enter_intro_date(date)
    else:
        context.discon_date = date
        page.enter_disc_date(date)

@given('the user selects {Company} company')
def step_impl(context, company):
    if company == "null":
        pass
    else:
        page = CreatePage(context.browser)
        page.select_company(company)












# Thens

@then('the user will be navigated to "Create_Computer" page')
def step_impl(context):
    page = CreatePage(context.browser)
    assert page.isat_createpage(), "Not at ADD Computer page"









