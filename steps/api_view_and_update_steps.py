from behave import given, when, then
from modules.api.api import API

@when('a user updates record with name "<Computer_name>", intro_date "<Introduced_Date>", discon_date "<Discontinued_Date>" and company "<Company>"')
def step_impl(context, Computer_name, Introduced_Date, Discontinued_Date, Company):
    context.updated_computer_name = Computer_name
    context.updated_intro_date = Introduced_Date
    context.updated_discon_date = Discontinued_Date
    context.updated_company = Company
    context.api = API()

    context.api.update_computer(Computer_name, Introduced_Date, Discontinued_Date, Company, context.computer_url)