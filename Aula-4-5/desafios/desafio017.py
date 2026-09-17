from rich import print
from rich.align import Align
from rich.panel import Panel


class Produto:
    def __init__(self, nome, preco) -> None:
        self.nome = nome
        self.preco = preco


    def etiqueta(self):
        texto = f"{self.nome.center(30, ' ')}"
        texto += f"{'-' * 30}"
        pf = f"R${self.preco:,.2f}"
        texto += f"{pf.center(30, '.')}"
        painel = Panel(texto, title="Produto", width=34)
        print(painel)


p1 = Produto("iPhone 17 Pro Max", 25000)
p1.etiqueta()