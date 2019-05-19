from behave import given, when, then
from modules.pages.create_and_edit_page import CreateAndEditPage
from modules.pages.homepage import Homepage


@given('A user has created a computer with known details')
def step_impl(context):
    context.execute_steps('Given A user has navigated to the BB_Test_Webpage')
    page = Homepage(context.browser)
    page2 = CreateAndEditPage(context.browser)
    computer_name = "BB_computer_for_edit_test"
    while page.confirm_computer_present(computer_name):
        page.click_on_computer_name(computer_name)
        page2.click_delete_computer()
        if not (page.confirm_computer_present(computer_name)):
            break

    context.execute_steps('Given A user has navigated to the BB_Test_Webpage')
    context.execute_steps('Given add a new computer is clicked')
    context.execute_steps('Given the User enters BB_computer_for_edit_test computer name')
    context.execute_steps('Given the user enters 1986-04-04 introduced date')
    context.execute_steps('Given the user enters 2000-07-07 discontinued date')
    context.execute_steps('Given the user selects Apple Inc. company')
    context.execute_steps('When the user clicks Save_this_computer')



@given('the User updates {computer_name} computer name')
def step_impl(context, computer_name):
    page = CreateAndEditPage(context.browser)
    if computer_name != "null":
        context.updated_computer_name = computer_name
        page.enter_computer(computer_name)
    else:
        context.updated_computer_name = context.computer_name
        page.enter_computer(" ")


@given('the user updates {date} {format} date')
def step_impl(context, date, format):
    page = CreateAndEditPage(context.browser)
    if format == "introduced":
            if date != "null":
                context.updated_intro_date = date
                page.enter_intro_date(date)
            else:
                context.updated_intro_date = context.intro_date
                pass
    elif format == "discontinued":
            if date != "null":
                context.updated_discon_date = date
                page.enter_disc_date(date)
            else:
                context.updated_discon_date = context.discon_date
                pass


@given('the user updates {company} company')
def step_impl(context, company):
    if company != "null":
        context.updated_company = company
        page = CreateAndEditPage(context.browser)
        page.select_company(company)
    else:
        context.updated_company = context.company
        pass


@when('the user clicks save_this_computer')
def step_impl(context):
    page = CreateAndEditPage(context.browser)
    page.click_save()

@then('the user will be navigated to "Edit_Computer" page')
def step_impl(context):
    page = CreateAndEditPage(context.browser)
    assert page.isat_editpage(), "Not at add Edit page"
    page.click_cancel()


@then('the Computer will be updated')
def step_impl(context):
    page = Homepage(context.browser)
    assert page.computer_updated(context.updated_computer_name), "Computer not updated"

@then('the computer is updated on the table with the correct information')
def step_impl(context):
    name = context.updated_computer_name
    intro_date = context.updated_intro_date
    discon_date = context.updated_discon_date
    company = context.updated_company

    page = Homepage(context.browser)
    page.search_for_computer(name)
    assert page.computer_has_correct_date(name, intro_date, "intro"), "intro_date is incorrect"
    assert page.computer_has_correct_date(name, discon_date, "dison"), "discon_date is incorrect"
    assert page.computer_has_correct_company(name, company)


@then('the number of computers found will stay the same')
def step_impl(context):
    page = Homepage(context.browser)
    no_computers = context.computer_count

    assert page.computer_count() == (no_computers), "computer count changed"


@then('Delete computer cleanup edit')
def step_impl(context):
     page = Homepage(context.browser)
     page.goto_home_page()
     page.search_for_computer(context.updated_computer_name)
     page.click_on_computer_name(context.updated_computer_name)
     page = CreateAndEditPage(context.browser)
     page.click_delete_computer()

@then('Delete computer cleanup validation')
def step_impl(context):
     page = Homepage(context.browser)
     page.goto_home_page()
     page.search_for_computer(context.computer_name)
     page.click_on_computer_name(context.computer_name)
     page = CreateAndEditPage(context.browser)
     page.click_delete_computer()