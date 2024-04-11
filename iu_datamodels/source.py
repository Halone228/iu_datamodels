from .base import BaseModel
from .vein import Vein


class SourceBase(BaseModel):
    slug: str
    source_metadata: dict


class SourceShort(SourceBase):
    vein_id: int


class Source(SourceShort):
    id: int


class SourceFull(SourceBase):
    id: int
    vein: Vein


__all__ = [
    'SourceBase',
    'Source',
    'SourceShort',
    'SourceFull'
]