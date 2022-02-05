from pydantic import BaseModel as PydanticBaseModel


class BaseModel(PydanticBaseModel):
    class Config:
        orm_mode = True
        allow_population_by_field_name = True
