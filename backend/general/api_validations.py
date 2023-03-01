import logging

from assertpy import assert_that, soft_assertions
from pydantic import ValidationError


class ApiValidations:

    # region Success responses
    @staticmethod
    def status_response_200(response):
        try:
            assert_that(response.status_code).is_equal_to(200)
            assert_that(response.reason).is_equal_to('OK')
        except AssertionError:
            logging.error(f"Status error.\n Status: {response.status_code}\n Body: {response.json()}")
            raise
        else:
            logging.info(f"Status OK: {response.status_code}")

    # endregion

    # region Error responses
    @staticmethod
    def status_response_400(response, errors):
        try:
            assert_that(response.status_code).is_equal_to(400)
            assert_that(response.reason).is_equal_to('Bad Request')
            ApiValidations.validate_error_response_model(response, 'One or more errors have occurred.', errors)
        except AssertionError:
            logging.error(f"Status error.\n Status: {response.status_code}\n Body: {response.json()}")
            raise

    @staticmethod
    def status_response_401(response):
        try:
            assert_that(response.status_code).is_equal_to(401)
            assert_that(response.reason).is_equal_to('Unauthorized')
            ApiValidations.validate_error_response_model(response, 'One or more errors have occurred.',
                                                         ['Bearer Token is invalid.'])
        except AssertionError:
            logging.error(f"Status error.\n Status: {response.status_code}\n Body: {response.json()}")
            raise
    # endregion

    # region Validations
    @staticmethod
    def validate_error_response_model(response, message, errors):
        if response.text != "":
            with soft_assertions():
                try:
                    from backend.resources.models.error import ErrorModel
                    model = ErrorModel(**response.json())
                    assert_that(model.message).is_equal_to(message)
                    assert_that(model.errors).is_equal_to(errors)
                except ValidationError:
                    logging.error(f"Model error.\n Response body: {response.json()}")
                else:
                    logging.info("Response model: OK")
    # endregion
