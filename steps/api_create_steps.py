from behave import given, when, then
from modules.api.api import API


@given('a user creates a new record with name "{Computer_name}", intro_date "{Introduced_Date}", discon_date "{Discontinued_Date}" and company "{Company}"')
def step_impl(context, Computer_name, Introduced_Date, Discontinued_Date, Company):
    context.computer_name = Computer_name
    context.intro_date = Introduced_Date
    context.discon_date = Discontinued_Date
    context.company = Company
    context.api = API()

    context.api.create_computer(Computer_name, Introduced_Date, Discontinued_Date, Company)

@then('the response status should be {response_code}')
def step_impl(context, response_code):
    assert context.api.confirm_response_code(response_code)

@then('the computer will be visible in the UI')
def step_impl(context,):
    context.execute_steps('Given A user has navigated to the BB_Test_Webpage')
    context.execute_steps('Then the computer has been added to the table with the correct information')
    context.execute_steps('Then Delete computer cleanup create')
