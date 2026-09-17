from rich import print
from rich.panel import Panel


class Controle:
    def __init__(self) -> None:
        while True:
            texto = "[red]🛑 A TV está Desligada[/]"
            painel = Panel(texto, title=" [ TV ] ", width=30)
            print(painel)
            self.botao = input("")


Controle()