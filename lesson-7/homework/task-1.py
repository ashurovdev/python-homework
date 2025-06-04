import math
from typing import Iterable, Iterator, Union

number = Union[int, float]

class Vector:
    def __init__(self, *components: number):
        if not components:
            raise ValueError('Vektor kamida bitta komponent bo\'lishi lozim')
        if not all(isinstance(c, (int, float)) for c in components):
            raise TypeError('Vektor komponentlari son bo\'lishi lozim')
        self._components = tuple(float(c) for c in components)

    def to_string(self):
        comps = ','.join(self._format(c) for c in self._components)
        return f'Vector({comps})'        
    
    def get_length(self):
        return len(self._components)
    
    def iteract(self):
        return iter(self._components)
    
    def get_item(self, idx: int):
        return self._components[idx]
    
    def is_equal(self, other: object):
        return isinstance(other, Vector) and self._components == other._components
    
    def _check_dim(self, other: "Vector"):
        if self.get_length() != other.get_length():
            raise ValueError('Vektorlar satr va ustunlari bir xil bo\'lishi kerak')
        
    def add(self, other: 'Vector'):
        self._check_dim(other)
        return Vector(*(a+b for a,b in zip(self._components, other._components)))
    
    def subtract(self, other: 'Vector'):
        self._check_dim(other)
        return Vector(*(a-b for a,b in zip(self._components, other._components)))
    
    def dot_product(self, other: 'Vector'):
        self._check_dim()
        return sum(a*b for a,b in zip(self._components, other._components))
    
    def scalar_multiply(self, scalar: number):
        if not isinstance(scalar, (int, float)):
            raise TypeError('Skalar son bo\'lishi kerak')
        return Vector(*(scalar * a for a in self._components ))
    
    def magnitude(self):
        return math.sqrt(sum(a*a for a in self._components))
    
    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            raise ValueError('Normal qilib bo\'lmaydi')
        return Vector(*(a/mag for a in self._components))
    
    @staticmethod
    def _format(value: float):
        formatted = f'{value:.3f}'
        formatted = formatted.rstrip('0').rstrip('.')
        return formatted