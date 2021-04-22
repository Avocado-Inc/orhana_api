from typing import Type

from pydantic import BaseModel
from pydantic import Extra
from pydantic.utils import GetterDict


class BaseDbResponse(BaseModel):
    def simple_dict(self):
        return self.dict(exclude_none=True, exclude_unset=True)

    class Config:
        orm_mode = True
        getter_dict: Type[GetterDict] = GetterDict
        anystr_strip_whitespace = True
        validate_assignment = True
        validate_all = True
        extra = Extra.ignore
