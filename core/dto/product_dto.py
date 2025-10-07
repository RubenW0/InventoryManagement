# core/dtos.py
from dataclasses import dataclass

@dataclass
class ProductDTO:
    id: int
    name: str
    price: float
    stock: int

@dataclass
class ProductCreateDTO:
    name: str
    price: float
    stock: int
