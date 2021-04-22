from pydantic import BaseModel
from pydantic import Extra


class BaseDto(BaseModel):
    def simple_dict(self):
        return self.dict(exclude_none=True, exclude_unset=True)

    class Config:
        anystr_strip_whitespace = True
        validate_all = True
        extra = Extra.forbid
