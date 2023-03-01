import allure
import pytest

from backend.apis.menu import MenuAPI
from backend.general.api_validations import ApiValidations

pytestmark = [
    allure.parent_suite('Backend'),
    allure.suite('MenuAPI')
]


@pytest.mark.API
class TestGetId:
    """
    API – Menu – Get departments
    """

    # region Setup
    def setup_class(self):
        self.menu_api = MenuAPI()
    # endregion

    # region Tests - Status 200
    def test_get_departments_successfully(self):
        """
        Verify response with successful execution
        """
        response = self.menu_api.get_departments()
        ApiValidations.status_response_200(response)
        self.menu_api.validate_response_model_get_departments(response)
    # endregion

    # region Tests - Status 400
    def test_get_departments_unspecific_extra_parameter(self):
        """
        TC-
        Verify response with unspecific extra parameter
        """
        response = self.menu_api.get_departments(extra='test')
        ApiValidations.status_response_400(response, ["'extra' is unknown property."])
    # endregion

    # region Tests - Status 401
    def test_get_departments_wrong_token(self):
        """
        TC-
        Verify response when executing with wrong token
        """
        response = self.menu_api.get_departments('wrong token')
        ApiValidations.status_response_401(response)
    # endregion
