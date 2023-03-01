import logging

from assertpy import assert_that

from frontend.general.web_tasks import WebTasks


class WebValidations:

    @staticmethod
    def validate_text(driver, label, text):
        label = WebTasks.get_element(driver, label)
        try:
            assert_that(text).is_equal_to(label.text)
            logging.info(f"Text is: '{text}'.")
        except AssertionError:
            logging.error("Expected: '%s'. And got: '%s'", text, label.text)
            raise

    @staticmethod
    def validate_url(driver, url):
        try:
            assert_that(driver.current_url).is_equal_to(url)
            logging.info(f"Url is: '{url}'.")
        except AssertionError:
            logging.error("Expected: '%s'. And got: '%s'", url, driver.current_url)
            raise

    @staticmethod
    def is_not_visible(driver, locator):
        is_visible = bool(driver.find_elements(*locator))
        try:
            assert_that(not is_visible)
        except AssertionError:
            logging.error("Element is visible: ", locator)
            raise
