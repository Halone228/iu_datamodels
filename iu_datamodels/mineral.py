from .base import BaseModel
from .source import *
from datetime import datetime
from fastapi import UploadFile


attachment_id_type = str


class MineralBase(BaseModel):
    id: int
    html_text: str
    created_at: datetime


class Mineral(MineralBase):
    source_id: int


class MineralAndSource(MineralBase):
    source: SourceFull


class AttachmentRaw(BaseModel):
    file: UploadFile
    hash: str


class Attachments(BaseModel):
    attachments: list[attachment_id_type]


class MineralAndAttachments(Mineral, Attachments):
    pass


class MineralFull(MineralAndSource, Attachments):
    pass


__all__ = [
    "Mineral",
    "MineralAndSource",
    "MineralAndAttachments",
    "MineralFull",
    "AttachmentRaw",
    "attachment_id_type",
]
