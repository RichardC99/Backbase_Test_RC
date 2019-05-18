from behave import given
from modules.pages.homepage import Homepage
from modules.pages.create_and_edit_page import CreateAndEditPage
from time import sleep



@given('A user has navigated to the BB_Test_Webpage')
def step_impl(context):
    page = Homepage(context.browser)
    page.goto_home_page()
    context.no_of_computers_start = page.computer_count()


@given('add a new computer is clicked')
def step_impl(context):
    page = Homepage(context.browser)
    page.click_add_computer_button()


@given('the user selects {company} company')
def step_impl(context, company):
    context.company = company
    if company != "null":
        page = CreateAndEditPage(context.browser)
        page.select_company(company)
    else:
        pass
