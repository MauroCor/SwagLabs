import logging

from selenium.webdriver.common.by import By

from frontend.general.web_tasks import WebTasks

# region Field
FIELD_USERNAME = (By.ID, "user-name")
FIELD_PASSWORD = (By.ID, "password")
# endregion

# region Button
BUTTON_LOGIN = (By.ID, "login-button")
# endregion

# region Label
LABEL_VALIDATION = (By.XPATH, "//h3[@data-test='error']")
# endregion


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    # region Actions
    def log_in(self, user, password):
        logging.info(f"Credentials: {user}, {password}.")
        WebTasks.send_keys(self.driver, user, FIELD_USERNAME)
        WebTasks.send_keys(self.driver, password, FIELD_PASSWORD)
        WebTasks.click(self.driver, BUTTON_LOGIN)
    # endregion
