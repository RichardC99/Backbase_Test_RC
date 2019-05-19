from behave import given, when, then
from modules.api.api import API


@given('a user creates a new computer named {Computer_name} via the API')
def step_impl(context, computer_name):
    context.api =API()
