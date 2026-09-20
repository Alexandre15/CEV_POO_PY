from abc import ABC, abstractmethod
from math import pi


class Poligono(ABC):
    def __init__(self, qtd_lados) -> None:
        self.qtd_lados = qtd_lados

    @abstractmethod
    def perimetro():
        pass

    @abstractmethod
    def area():
        pass

class Quadrado(Poligono):
    def __init__(self, lado = 1) -> None:
        super().__init__(4)
        self.lado = lado

    def perimetro(self):
        return self.lado * self.qtd_lados

    def area(self):
        return self.lado ** 2

class Circulo(Poligono):
    def __init__(self, raio = 1) -> None:
        super().__init__(0)
        self.raio = raio

    def perimetro(self) -> float:
        return 2 * pi * self.raio

    def area(self) -> float:
        return pi * (self.raio ** 2)
