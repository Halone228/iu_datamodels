from pydantic import BaseModel as bm, ConfigDict


class BaseModel(bm):
    model_config = ConfigDict(
        from_attributes=True
    )
