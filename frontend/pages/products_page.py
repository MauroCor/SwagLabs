import logging

from selenium.webdriver.common.by import By

from frontend.general.web_tasks import WebTasks
from frontend.pages.web_general_page import WebGeneralPage

# region Button
BUTTON_CART = (By.XPATH, "//a[@class='shopping_cart_link']")
# endregion

# region Label
LABEL_CART_COUNTER = (By.XPATH, "//span[@class='shopping_cart_badge']")
LABEL_TITLE = (By.XPATH, "//span[@class='title']")
# endregion


class ProductsPage:

    def __init__(self, driver):
        self.driver = driver

    # region Actions
    def add_to_cart(self, product):
        logging.info(f"Add product: {product}")
        WebTasks.click(self.driver, WebGeneralPage.elem("PRODUCT-BUTTON", product))

    def remove_to_cart(self, product):
        logging.info(f"Remove product: {product}")
        WebTasks.click(self.driver, WebGeneralPage.elem("PRODUCT-BUTTON", product))
    # endregion
