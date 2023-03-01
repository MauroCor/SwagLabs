import logging

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from config_loader import read_config_from_current_env


class WebTasks:

    @staticmethod
    def open_site(driver, site):
        url = read_config_from_current_env(site)
        driver.get(url)

    @staticmethod
    def get_element(driver, locator, timeout=5):
        try:
            element = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(locator))
        except (NoSuchElementException, TimeoutException):
            logging.info(f"Not found: '{locator[1]}'.")
        else:
            return element

    @staticmethod
    def click(driver, element):
        element = WebTasks.get_element(driver, element)
        return element.click()

    @staticmethod
    def send_keys(driver, text, field):
        element = WebTasks.get_element(driver, field)
        return element.send_keys(text)
