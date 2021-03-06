from behave import then
from modules.pages.homepage import Homepage
from modules.pages.create_and_edit_page import CreateAndEditPage


@then('the number of computers found will {incdec} by {n}')
def step_impl(context,incdec, n):
    page = Homepage(context.browser)

    if incdec == "decrease":
        n = -int(n)
        no_computers = context.computer_count
    else:
        n = int(n)
        no_computers = context.no_of_computers_start

    assert page.computer_count() == (no_computers + n), "computer count not changed"


@then('the user will be navigated back to the homepage')
def step_impl(context):
    page = Homepage(context.browser)
    assert page.isat_homepage(), "not at homepage"


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
