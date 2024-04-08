from .base import BaseModel


class VeinShort(BaseModel):
    name: str
    url: str


class Vein(VeinShort):
    id: int
    name: str
    url: str



__all__ = [
    'Vein'
]