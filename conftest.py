import json
import os
import pathlib
from distutils import util

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture()
def driver(request):
    if request.cls.pytestmark[0].name == 'WEB':
        config = configuration()
        headless = util.strtobool(os.environ.get('headless'))
        driver = None
        browser = config["browser"]
        if browser == 'Chrome':
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--lang=en")
            chrome_options.add_argument("--incognito")
            if headless:
                chrome_options.add_argument('--headless')
            driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
        elif browser == 'MicrosoftEdge':
            edge_options = webdriver.EdgeOptions()
            edge_options.add_argument("--lang=en")
            edge_options.add_argument("--incognito")
            if headless:
                edge_options.add_argument('--headless')
            driver = webdriver.Edge(EdgeChromiumDriverManager().install(), options=edge_options)
        driver.implicitly_wait(config["implicitly_wait"])
        driver.maximize_window()
        yield driver
        if request.node.rep_setup.passed:
            if request.node.rep_call.failed:
                # take screenshot
                file_name = request.node.name
                driver.save_screenshot(f"{pathlib.Path(__file__).parent.absolute()}/_screenshots/{file_name}.png")
                # attach screenshot to allure report
                allure.attach(driver.get_screenshot_as_png(), name=file_name, attachment_type=AttachmentType.PNG)
        driver.quit()


def pytest_addoption(parser):
    parser.addoption('--env', action='store', default='tst')
    parser.addoption('--headless', action='store', default='true')


def pytest_configure(config):
    os.environ["env"] = config.getoption('env')
    os.environ["headless"] = config.getoption('headless')


def configuration():
    config_path = str(pathlib.Path(__file__).parent.absolute()) + '/config.json'
    with open(config_path) as config_file:
        config = json.load(config_file)
    return config


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    """
    Check if a test has failed and set a report attribute.
    :param item: request.node
    :return: item.setup/call/teardown.passed/failed
    """
    outcome = yield
    if item.cls.pytestmark[0].name == 'WEB':
        rep = outcome.get_result()
        setattr(item, "rep_" + rep.when, rep)
