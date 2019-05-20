from behave import given, when, then
from modules.api.api import API

@when('The Computer is Deleted via the API')
def step_impl(context):
    context.api = API()
    context.api.delete_computer(context.computer_url)