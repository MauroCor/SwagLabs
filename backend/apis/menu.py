import logging

from pydantic import ValidationError

from backend.general.api_tasks import ApiTasks
from backend.resources.models.menu import MenuModelGetDepartments


class MenuAPI:

    @staticmethod
    def path():
        path = '/menu'
        return path

    # region Methods
    def get_departments(self, *scenario, **query_params):
        endpoint = f'{self.path()}/departments'
        response = ApiTasks.scenario_constructor(method='GET', endpoint=endpoint, scenario=scenario,
                                                 query_params=query_params)
        return response
    # endregion

    # region MenuAPI functions
    @staticmethod
    def validate_response_model_get_departments(response):
        try:
            model = MenuModelGetDepartments(**response.json())
        except ValidationError:
            logging.error(f"Model error.\n Response body: {response.json()}")
            raise
        else:
            logging.info("Response model: OK")
            return model
    # endregion
