from abc import ABC, abstractmethod


# =========================================== #
# --------------- CLASSE BASE --------------- #
# =========================================== #
class Transporte(ABC):
    def __init__(self, dist) -> None:
        super().__init__()
        self.distancia = dist
        self.frete = ""

    @abstractmethod
    def calc_frete(self):
        pass

# =========================================== #
# --------------- SUB-CLASSES --------------- #
# =========================================== #
class Moto(Transporte):
    # Livre
    def __init__(self, dist) -> None:
        super().__init__(dist)
        self.fator = 0.50

    def calc_frete(self):
        return f"[green]R${self.distancia * self.fator:,.2f}[/]"

class Caminhao(Transporte):
    # No mínimo 50Km
    def __init__(self, dist) -> None:
        super().__init__(dist)
        self.fator = 1.20

    def calc_frete(self):
        if self.distancia < 50:
            return "[red]Raio mínimo de 50Km[/]"
        else:
            return f"[green]R${self.distancia * self.fator:,.2f}[/]"

class Drone(Transporte):
    # No máximo 10Km
    def __init__(self, dist) -> None:
        super().__init__(dist)
        self.fator = 9.50

    def calc_frete(self):
        if self.distancia > 10:
            return "[red]Raio máximo de 10Km[/]"
        else:
            return f"[green]R${self.distancia * self.fator:,.2f}[/]"