from .base import BaseModel


class Vein(BaseModel):
    id: int
    name: str
    url: str


__all__ = [
    'Vein'
]