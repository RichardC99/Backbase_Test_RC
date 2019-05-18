from behave import given, when, then
from modules.pages.create_and_edit_page import CreateAndEditPage
from modules.pages.homepage import Homepage



# Givens
@given('the User enters {computer_name} computer name')
def step_impl(context, computer_name):
    context.page = CreateAndEditPage(context.browser)
    context.computer_name = computer_name
    if computer_name != "null":
        context.page.enter_computer(computer_name)
    else:
        pass
    # context.janitors.append(CleanUpAfterTest())


@given('the user enters {date} {format} date')
def step_impl(context, date, format):
    page = CreateAndEditPage(context.browser)
    if date != "null":
        if format == "introduced":
            context.intro_date = date
            page.enter_intro_date(date)
        else:
            context.discon_date = date
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



@when('the user clicks Save_this_computer')
def step_impl(context):
    page = CreateAndEditPage(context.browser)
    page.click_Create()

@when('the user clicks cancel')
def step_impl(context):
    page = CreateAndEditPage(context.browser)
    page.click_cancel()

# Thens

@then('the user will be navigated to "Create_Computer" page')
def step_impl(context):
    page = CreateAndEditPage(context.browser)
    assert page.isat_Createpage(), "Not at add Computer page"

@then('the user will be navigated back to the homepage')
def step_impl(context):
    page = Homepage(context.browser)
    assert page.isat_homepage(), "not at homepage"

@then('the user will remain at the add computer screen')
def step_impl(context):
    page = CreateAndEditPage(context.browser)
    assert page.isat_Createpage(), "Not at add computer page"

@then('the Computer will be created')
def step_impl(context):
    page = Homepage(context.browser)
    assert page.computer_created(context.computer_name), "Computer not created"

@then('the computer has been added to the table with the correct information')
def step_impl(context):
    name = context.computer_name
    intro_date = context.intro_date
    discon_date = context.discon_date
    company = context.company

    page = Homepage(context.browser)
    page.search_for_computer(name)
    assert page.computer_has_correct_date(name, intro_date, "intro"), "date is incorrect"
    assert page.computer_has_correct_date(name, discon_date, "dison"), "date is incorrect"
    assert page.computer_has_correct_company(name, company)
    

@then('the correct error message will appear {error}')
def step_impl(context, error):
    page = CreateAndEditPage(context.browser)
    if error == "name_required":
        assert page.invalid_name_error(), "error message not present"

    elif error == "invalid_intro_date_format":
        assert page.invalid_intro_date_format(), "error message not present"

    elif error == "invalid_discon_date_format":
        assert page.invalid_discon_date_format(), "error message not present"

    elif error == "all_data_invalid":
        assert page.invalid_name_error(), "error message not present"
        assert page.invalid_intro_date_format(), "error message not present"
        assert page.invalid_discon_date_format(), "error message not present"

# def cleanup(context):
#     page = Homepage(context.browser)
#     page.enter_into_filter_by_name_input(context.computer_name)
#     page.click_filter_by_name_button()
#     page.click_on_computer_name(context.computer_name)
#     page = EditPage(context.browser)
#     page.click_delete_computer()



# class CleanUpAfterTest(AbstractJanitor):
#     def __init__(self):
#         self = self
#
#     def clean_up(self):
#         cleanup(self.)
#








