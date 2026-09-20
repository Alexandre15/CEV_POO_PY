from abc import ABC, abstractmethod


# =========================================== #
# --------------- CLASSE BASE --------------- #
# =========================================== #
class Transporte(ABC):
    def __init__(self, dist) -> None:
        super().__init__()
        self.distancia = dist
        self.frete = 0

    @abstractmethod
    def calc_frete(self):
        pass

# =========================================== #
# --------------- SUB-CLASSES --------------- #
# =========================================== #
class Moto(Transporte):
    # Livre
    fator = 0.50
    def __init__(self, dist) -> None:
        super().__init__(dist)

    def calc_frete(self):
        self.frete = self.distancia * Moto.fator
        return f"[green]R${self.frete:,.2f}[/]"

class Caminhao(Transporte):
    # No mínimo 50Km
    fator = 1.20
    def __init__(self, dist) -> None:
        super().__init__(dist)

    def calc_frete(self):
        if self.distancia < 50:
            self.frete = 0
            return "[red]Raio mínimo de 50Km[/]"
        else:
            self.frete = self.distancia * Caminhao.fator
            return f"[green]R${self.frete:,.2f}[/]"

class Drone(Transporte):
    # No máximo 10Km
    fator = 9.50
    def __init__(self, dist) -> None:
        super().__init__(dist)

    def calc_frete(self):
        if self.distancia > 10:
            self.frete = 0
            return "[red]Raio máximo de 10Km[/]"
        else:
            self.frete = self.distancia * Drone.fator
            return f"[green]R${self.frete:,.2f}[/]"