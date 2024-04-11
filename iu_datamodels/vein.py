from .base import BaseModel


class VeinShort(BaseModel):
    name: str
    url: str
    slug: str


class Vein(VeinShort):
    id: int


__all__ = [
    'Vein',
    'VeinShort'
]