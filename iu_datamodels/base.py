from pydantic import BaseModel as bm, ConfigDict


class BaseModel(bm):
    config: ConfigDict = {
        'from_attributes': True
    }
