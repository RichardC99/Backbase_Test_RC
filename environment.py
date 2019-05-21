from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import os
import datetime
import config
import traceback



def before_feature(context, feature):
    pass


def before_scenario(context, scenario):
    if "web" in context.tags:
        if not getattr(context, 'browser', None):
            setup_browser(context)

    context.janitors = []


def after_feature(context, feature):
    if getattr(context, 'browser', None):
        close_browser(context)


def after_scenario(context, scenario):

    try:
        if getattr(context, 'browser', None):
            if scenario.status == "failed":
                if not os.path.exists("failed_scenarios_screenshots"):
                    os.makedirs("failed_scenarios_screenshots")

                t = datetime.datetime.now()
                file_name = f"{scenario.name.replace(' ', '_')}_{t.strftime('%Y%d%m%H%M%S%f')}.png"
                file_path = os.path.join("failed_scenarios_screenshots", file_name)
                print(f"screenshot saved to {file_path}")

                context.browser.save_screenshot(file_path)

            close_browser(context)
    except Exception as e:
        print(f"exception cleaning up after web scenario")
        traceback.print_exc()

    for janitor in context.janitors:
        print("Janitor for scenario from list, calling clean up")
        try:
            janitor.clean_up()
        except Exception as e:
            print(f"exception running janitor")
            traceback.print_exc()


def setup_browser(context):
    driver = getattr(config, 'driver', 'chrome')
    driver_path = getattr(config, '{}_driver_path'.format(driver), '')

    if "chrome" == driver:
        options = ChromeOptions()
        options.add_argument("--window-position=2000,0")
        #use below path for Windows/Linux machines along with the correct config file

        #context.browser = webdriver.Chrome(executable_path=driver_path, chrome_options=options)

        #use the below path for OSX machines, along with the corretc config file

        context.browser = webdriver.Chrome()

    elif "firefox" == driver:
        options = FirefoxOptions()
        options.add_argument("--window-position=2000,0")

    else:
        raise ValueError(f"invalid browser specified [{driver}]")

    context.browser.maximize_window()


def close_browser(context):
    print("closing browser")
    context.browser.close()
    context.browser = None





