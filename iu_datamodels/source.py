from .base import BaseModel
from .vein import Vein


class SourceBase(BaseModel):
    id: int
    uname: str
    metadata: dict


class SourceShort(SourceBase):
    vein_id: int


class SourceFull(SourceBase):
    vein: Vein


__all__ = [
    'SourceShort',
    'SourceFull'
]