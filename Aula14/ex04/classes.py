from ast import Try

from rich import print


class Numero:
    def __init__(self, valor: float = 0) -> None:
        self.valor = valor

    def dobrar(self):
        self.valor *= 2

    def __str__(self) -> str:
        return f"Tenho o valor {self.valor} dentro do Número."


class Texto:
    def __init__(self, txt: str = "") -> None:
        self.texto = txt

    def dobrar(self):
        self.texto += " " + self.texto

    def __str__(self) -> str:
        return f"Tenho o texto '{self.texto}' dentro do Texto."


class Lista:
    def __init__(self, lst: list = []) -> None:
        self.valores = lst

    def dobrar(self):
        for e, d in enumerate(self.valores):
            self.valores[e] *= 2

    def __str__(self) -> str:
        return f"Tenho os itens {self.valores} dentro da Lista."
    

class Papel:
    def __init__(self) -> None:
        self.dobrado = False

    def dobrar(self):
        self.dobrado = True

    def __str__(self) -> str:
        return f"O papel está {'novo' if not self.dobrado else 'dobrado'}"


class Casa:
    def __init__(self) -> None:
        pass

    def __str__(self) -> str:
        return "Era uma casa, muito engraçada..."


# METODO PYTHONICO POLIMORFICO DUCK TYPING

def tente_dobrar(objeto):
    try:
        objeto.dobrar()
    except AttributeError:
        print(f"Tive dificuldades para dobrar {objeto.__class__.__name__}")