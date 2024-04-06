from .base import BaseModel


class TagShort(BaseModel):
	descriptor: str


class Tag(TagShort):
	id: int
