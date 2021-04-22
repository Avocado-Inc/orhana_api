from typing import Dict
from typing import Generic
from typing import Optional

from pydantic.generics import GenericModel
from pydantic.generics import TypeVar
from pydantic.main import Extra

Data = TypeVar("Data")


class BaseResponse(GenericModel, Generic[Data]):
    code: int
    message: str
    data: Data
    meta: Optional[Dict]

    def simple_dict(self):
        return self.dict(exclude_unset=True, exclude_none=True)

    class Config:
        orm_mode = True
        anystr_strip_whitespace = True
        validate_all = True
        extra = Extra.forbid
        validate_assignment = True
