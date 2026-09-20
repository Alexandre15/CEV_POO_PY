from abc import ABC, abstractmethod
from random import randint

from rich import print


class Personagem(ABC):
    def __init__(self, nome, vida) -> None:
        super().__init__()
        self.nome = nome
        self.vida = vida
        self.golpes = list("")

    @abstractmethod
    def curar(self):
        pass

    def atacar(self, alvo, forca):
        tm = len(self.golpes)
        print(f"[green]{self.nome}[/]({self.vida}) atacou {alvo.nome}({alvo.vida}) com um [blue]{self.golpes[randint(0, tm-1)]}[/] força {forca}.")
        dano = randint(0, forca)
        alvo.receber_dano(dano)

    def receber_dano(self, dano):
        print(f"[blue]{self.nome}[/] recebeu [red]dano de {dano}![/]")


class Guerreiro(Personagem):
    def __init__(self, nome, vida) -> None:
        super().__init__(nome, vida)
        self.golpes = ["Soco", "Golpe giratório", "Espadada Grossa", "Garoto"]

    def curar(self):
        print(f"[blue]{self.nome}[/] enrolou uma atadura nos ferimentos e [green]recuperou {randint(0, 100)} pontos[/] de vida.")


class Mago(Personagem):
    def __init__(self, nome, vida) -> None:
        super().__init__(nome, vida)
        self.golpes = ["Poderzinho", "Varada", "A vara que raba", "Nós que know"]

    def curar(self):
        print(f"[blue]{self.nome}[/] fez uma magia de cura e [green]recuperou {randint(0, 100)} pontos[/] de vida.")