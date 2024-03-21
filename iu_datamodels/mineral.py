from .base import BaseModel
from .source import *
from datetime import datetime


class MineralBase(BaseModel):
    id: int
    html_text: str
    created_at: datetime


class Mineral(MineralBase):
    source_id: int


class MineralAndSource(MineralBase):
    source: SourceFull


class Attachments(BaseModel):
    attachments: list[str]


class MineralAndAttachments(Mineral, Attachments):
    pass


class MineralFull(MineralAndSource, Attachments):
    pass


__all__ = [
    'Mineral',
    'MineralAndSource',
    'MineralAndAttachments',
    'MineralFull'
]
