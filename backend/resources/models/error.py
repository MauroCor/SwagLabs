from pydantic import BaseModel
from pydantic.class_validators import List


class ErrorModel(BaseModel):
    message: str
    errors: List[str]
