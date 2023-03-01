from pydantic import BaseModel
from pydantic.class_validators import List, Optional


class ChildrenCategories(BaseModel):
    id: str
    name: Optional[str]
    permalink: str


class Categories(BaseModel):
    id: str
    name: str
    permalink: str
    children_categories: List[ChildrenCategories]


class Departments(BaseModel):
    name: str
    categories: List[Categories]


class Landings(BaseModel):
    label: str
    permalink: str


class MoreCategories(BaseModel):
    label: str
    permalink: str


class HighPriority(BaseModel):
    label: str
    permalink: str


class MenuModelGetDepartments(BaseModel):
    departments: List[Departments]
    landings: List[Landings]
    more_categories: MoreCategories
    high_priority: List[HighPriority]
