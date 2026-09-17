from rich import print
from rich.align import Align
from rich.panel import Panel


class Gamer:
    def __init__(self, nome, nick) -> None:
        self.nome = nome
        self.nick = nick
        self.favoritos = []


    def add_favorito(self, favorito):
        self.favoritos.append(favorito)


    def ficha(self):
        fav = sorted(self.favoritos)
        texto = Align.left(f"Nome real: [white on blue]{self.nome}[/]\nJogos favoritos:\n:video_game: "+"\n:video_game: ".join(fav))
        painel = Panel(texto, title=f"{self.nome} <{self.nick}>", width=50)
        print(painel)


j1 = Gamer("Alexandre", "R3tr0")
j1.add_favorito("Assassins Creed")
j1.add_favorito("Asseto Corsa")
j1.add_favorito("Minecraft")
j1.ficha()