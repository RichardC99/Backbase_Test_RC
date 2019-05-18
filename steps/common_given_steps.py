from behave import given
from modules.pages.homepage import Homepage
from modules.pages.create_and_edit_page import CreateAndEditPage


@given('A user has created a computer with known details and navigated to the edit screen')
def step_impl(context):
    context.execute_steps('Given A user has navigated to the BB_Test_Webpage')
    context.execute_steps('Given add a new computer is clicked')
    context.execute_steps('Given the User enters BB_computer_for_edit_test computer name')
    context.execute_steps('Given the user enters 1986-04-04 introduced date')
    context.execute_steps('Given the user enters 2000-07-07 discontinued date')
    context.execute_steps('Given the user selects Apple Inc. company')
    context.execute_steps('When the user clicks Save_this_computer')
    context.execute_steps('the User navigates to the Update Computer screen')

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
    page.search_for_computer(context.computer_name)
    page.click_on_computer_name(context.computer_name)


@given('the User enters {computer_name} computer name')
def step_impl(context, computer_name):
    context.page = CreateAndEditPage(context.browser)
    context.computer_name = computer_name
    if computer_name != "null":
        context.page.enter_computer(computer_name)
    else:
        pass


@given('the user enters {date} {format} date')
def step_impl(context, date, format):
    page = CreateAndEditPage(context.browser)
    if format == "introduced":
            context.intro_date = date
            if date != "null":
                page.enter_intro_date(date)
            else:
                pass
    elif format == "discontinued":
            context.discon_date = date
            if date != "null":
                page.enter_disc_date(date)
            else:
                pass


@given('the user selects {company} company')
def step_impl(context, company):
    context.company = company
    if company != "null":
        page = CreateAndEditPage(context.browser)
        page.select_company(company)
    else:
        pass
