import allure
import pytest

from frontend.general.web_tasks import WebTasks
from frontend.general.web_validations import WebValidations
from frontend.pages import products_page
from frontend.pages.login_page import LoginPage
from frontend.pages.products_page import ProductsPage
from frontend.pages.web_general_page import WebGeneralPage

pytestmark = [
    allure.parent_suite('FrontEnd'),
    allure.suite('AddToCart'),
]


@pytest.mark.WEB
class TestAddToCart:

    @pytest.mark.SMOKE
    def test_add_product_to_cart(self, driver):
        """
        TC-03 - Add to cart - Agregar producto al carrito.
        """
        WebTasks.open_site(driver, "saucedemo")
        LoginPage(driver).log_in("standard_user", "secret_sauce")
        ProductsPage(driver).add_to_cart("Sauce Labs Backpack")
        WebValidations.validate_text(driver, WebGeneralPage.elem("PRODUCT-BUTTON", "Sauce Labs Backpack"), "Remove")
        WebValidations.validate_text(driver, products_page.LABEL_CART_COUNTER, "1")
        WebTasks.click(driver, products_page.BUTTON_CART)
        WebValidations.validate_text(driver, WebGeneralPage.elem("PRODUCT-BUTTON", "Sauce Labs Backpack"), "Remove")

    def test_remove_product_to_cart(self, driver):
        """
        TC-04 - Add to cart - Eliminar producto del carrito.
        """
        WebTasks.open_site(driver, "saucedemo")
        LoginPage(driver).log_in("standard_user", "secret_sauce")
        ProductsPage(driver).add_to_cart("Sauce Labs Backpack")
        ProductsPage(driver).add_to_cart("Sauce Labs Bike Light")
        WebValidations.validate_text(driver, products_page.LABEL_CART_COUNTER, "2")
        WebTasks.click(driver, products_page.BUTTON_CART)
        ProductsPage(driver).remove_to_cart("Sauce Labs Backpack")
        WebValidations.is_not_visible(driver, WebGeneralPage.elem("PRODUCT-BUTTON", "Sauce Labs Backpack"))
        WebValidations.validate_text(driver, products_page.LABEL_CART_COUNTER, "1")
        WebTasks.click(driver, WebGeneralPage.elem("BUTTON", "Continue Shopping"))
        WebValidations.validate_text(driver, WebGeneralPage.elem("PRODUCT-BUTTON", "Sauce Labs Backpack"), "Add to cart")
        WebValidations.validate_text(driver, WebGeneralPage.elem("PRODUCT-BUTTON", "Sauce Labs Bike Light"), "Remove")
        ProductsPage(driver).remove_to_cart("Sauce Labs Bike Light")
        WebValidations.validate_text(driver, WebGeneralPage.elem("PRODUCT-BUTTON", "Sauce Labs Bike Light"), "Add to cart")
        WebValidations.is_not_visible(driver, products_page.LABEL_CART_COUNTER)
