from abc import ABC, abstractmethod
from math import pi


class Poligono(ABC):
    def __init__(self, qtd_lados = 4) -> None:
        self.qtd_lados = qtd_lados

    @abstractmethod
    def perimetro():
        pass

    @abstractmethod
    def area():
        pass

class Quadrado(Poligono):
    def __init__(self, lado) -> None:
        super().__init__()
        self.lado = lado

    def perimetro(self):
        return self.lado * self.qtd_lados

    def area(self):
        return self.lado ** 2

class Circulo(Poligono):
    def __init__(self, raio) -> None:
        super().__init__()
        self.raio = raio

    def perimetro(self):
        return 2 * pi * self.raio

    def area(self):
        return pi * (self.raio ** 2)
