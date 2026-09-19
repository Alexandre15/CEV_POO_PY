from abc import ABC, abstractmethod

from rich import print


class BebidaQuente(ABC):
    def __init__(self) -> None:
        super().__init__()

    def preparar(self):
        print("\n[blue]---------- Iniciando o Preparo ----------[/]\n")
        print(f"1. {self.ferver_agua()}")
        print(f"2. {self.misturar()}")
        print(f"3. {self.servir()}")
        print("\n[green]------------- Bebida Pronta -------------[/]\n")


    def ferver_agua(self):
        return "Ferver água a 100 graus Celsios"

    @abstractmethod
    def misturar(self):
        pass

    @abstractmethod
    def servir(self):
        pass

class Cafe(BebidaQuente):
    def __init__(self) -> None:
        super().__init__()

    def misturar(self):
        return "Passando água pressurizada pelo pó de café moido."

    def servir(self):
        return "Servindo em xícara pequena"

class Cha(BebidaQuente):
    def __init__(self) -> None:
        super().__init__()

    def misturar(self):
        return "Megulhando o sachê de ervas na água."

    def servir(self):
        return "Servindo na caneca de porcelana com limão."

class Leite(BebidaQuente):
    def __init__(self) -> None:
        super().__init__()

    def misturar(self):
        return "Passando vapor pressurizado pelo bico do leite."

    def servir(self):
        return "Servindo na caneca grande, já com café."
