from .base import BaseModel
from .source import *
from datetime import datetime
from fastapi import UploadFile


attachment_id_type = str


class MineralShort(BaseModel):
    html_text: str
    created_at: datetime
    tags: list[int]


class MineralBase(MineralShort):
    id: int


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


class MineralAndAttachmentsShort(MineralShort, Attachments):
    source_id: int


class MineralFull(MineralAndSource, Attachments):
    pass


__all__ = [
    "MineralAndAttachmentsShort",
    "Mineral",
    "MineralAndSource",
    "MineralAndAttachments",
    "MineralFull",
    "AttachmentRaw",
    "attachment_id_type",
]
