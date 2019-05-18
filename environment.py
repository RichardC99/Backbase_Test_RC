from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import os
import datetime
import config
import traceback


def before_feature(context, feature):
    pass


def before_scenario(context, scenario):
    # only launch a browser if tag @web and if there isn't one there already
    # this is needed in case browser was closed from a preceding failing scenario
    if "web" in context.tags:
        if not getattr(context, 'browser', None):
            setup_browser(context)

    # create an empty list of janitors ready for test steps to append specific clean up janitors to
    context.janitors = []


def after_feature(context, feature):
    # if there is a browser object close it
    if getattr(context, 'browser', None):
        close_browser(context)


def after_scenario(context, scenario):

    try:
        # if there is a browser object for a failing scenario grab a screenshot
        if getattr(context, 'browser', None):
            if scenario.status == "failed":
                if not os.path.exists("failed_scenarios_screenshots"):
                    os.makedirs("failed_scenarios_screenshots")

                t = datetime.datetime.now()
                file_name = f"{scenario.name.replace(' ', '_')}_{t.strftime('%Y%d%m%H%M%S%f')}.png"
                file_path = os.path.join("failed_scenarios_screenshots", file_name)
                print(f"screenshot saved to {file_path}")

                context.browser.save_screenshot(file_path)

            # close browser so clean for next scenario
            close_browser(context)
    except Exception as e:
        print(f"exception cleaning up after web scenario")
        traceback.print_exc()

    for janitor in context.janitors:
        print("Janitor for scenario from list, calling clean up")
        try:
            # if there is an exception running a janitor catch it and continue with the rest
            janitor.clean_up()
        except Exception as e:
            print(f"exception running janitor")
            traceback.print_exc()


def setup_browser(context):
    driver = getattr(config, 'driver', 'chrome')
    driver_path = getattr(config, '{}_driver_path'.format(driver), '')
    headless = getattr(config, 'headless', False)

    if "chrome" == driver:
        options = ChromeOptions()
        options.add_argument("--window-position=2000,0")
        if headless:
            options.add_argument('--headless')
        context.browser = webdriver.Chrome(executable_path=driver_path, chrome_options=options)

    elif "firefox" == driver:
        options = FirefoxOptions()
        if headless:
            options.add_argument('--headless')
        context.browser = webdriver.Firefox(executable_path=driver_path, firefox_options=options)
    else:
        raise ValueError(f"invalid browser specified [{driver}]")

    context.browser.maximize_window()


def close_browser(context):
    print("closing browser")
    context.browser.close()
    context.browser = None





