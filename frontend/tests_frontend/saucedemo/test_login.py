import allure
import pytest

from frontend.general.web_tasks import WebTasks
from frontend.general.web_validations import WebValidations
from frontend.pages import login_page, products_page
from frontend.pages.login_page import LoginPage

pytestmark = [
    allure.parent_suite('FrontEnd'),
    allure.suite('Login'),
]


@pytest.mark.WEB
class TestLogin:

    @pytest.mark.SMOKE
    def test_successful_login(self, driver):
        """
        TC-01 - Login - Login exitoso.
        """
        WebTasks.open_site(driver, "saucedemo")
        LoginPage(driver).log_in("standard_user", "secret_sauce")
        WebValidations.validate_url(driver, "https://www.saucedemo.com/inventory.html")
        WebValidations.validate_text(driver, products_page.LABEL_TITLE, "Productos")

    def test_wrong_credentials(self, driver):
        """
        TC-02 - Login - Credenciales incorrectas.
        """
        WebTasks.open_site(driver, "saucedemo")
        LoginPage(driver).log_in("", "")
        WebValidations.validate_text(driver, login_page.LABEL_VALIDATION, "Epic sadface: Username is required")
        LoginPage(driver).log_in("test_user", "")
        WebValidations.validate_text(driver, login_page.LABEL_VALIDATION, "Epic sadface: Password is required")
        LoginPage(driver).log_in("test_user", "secret_sauce")
        WebValidations.validate_text(driver, login_page.LABEL_VALIDATION,
                                     "Epic sadface: Username and password do not match any user in this service")
