from .base import BaseModel
from .vein import Vein


class SourceShort(BaseModel):
    id: int
    uname: str
    metadata: dict


class Source(SourceShort):
    vein_id: int


class SourceFull(SourceShort):
    vein: Vein


__all__ = [
    'SourceShort',
    'SourceFull'
]