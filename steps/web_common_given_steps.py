from behave import given
from modules.pages.homepage import Homepage
from modules.pages.create_and_edit_page import CreateAndEditPage


@given('the User navigates to the Update Computer screen')
def step_impl(context):
    page = Homepage(context.browser)
    context.computer_count = page.computer_count()
    page.search_for_computer(context.computer_name)
    page.click_on_computer_name(context.computer_name)
    context.computer_url = CreateAndEditPage(context.browser).get_page_url()


@given('A user has navigated to the BB_Test_Webpage')
def step_impl(context):
    page = Homepage(context.browser)
    page.goto_home_page()
    context.no_of_computers_start = page.computer_count()


@given('add a new computer is clicked')
def step_impl(context):
    page = Homepage(context.browser)
    page.click_add_computer_button()


@given('computer {computer_name} does not exist')
def step_impl(context, computer_name):
    page = Homepage(context.browser)
    page2 = CreateAndEditPage(context.browser)
    while page.confirm_computer_present(computer_name):
        page.click_on_computer_name(computer_name)
        page2.click_delete_computer()
        if not (page.confirm_computer_present(computer_name)):
            break
    context.execute_steps('Given A user has navigated to the BB_Test_Webpage')

@given('computer {Computer_name} does not exist for API testing')
def step_impl(context, Computer_name):
    context.execute_steps('Given A user has navigated to the BB_Test_Webpage')
    page = Homepage(context.browser)
    page2 = CreateAndEditPage(context.browser)
    while page.confirm_computer_present(Computer_name):
        page.click_on_computer_name(Computer_name)
        page2.click_delete_computer()
        if not (page.confirm_computer_present(Computer_name)):
            break

