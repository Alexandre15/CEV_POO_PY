from abc import ABC, abstractmethod
from random import randint, randrange

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
        if self.vida > 0 and alvo.vida > 0:
            golpe = self.golpes[randrange(0, len(self.golpes))]
            print(f"[green]{self.nome}[/]({self.vida}) atacou {alvo.nome}({alvo.vida}) com um [blue]{golpe}[/] força {forca}.")
            alvo.receber_dano(forca)
        else:
            print(f"O ataque {self.nome} -> {alvo.nome} não pode acontecer.")

    def receber_dano(self, dano):
        fator = randint(0, dano)
        self.vida -= fator
        self.vida = max(self.vida, 0) # essa expressão faz a mesma coisa que o if comentado abaixo 
        #if self.vida < 0:
        #    self.vida = 0
        print(f"[blue]{self.nome}[/] recebeu [red]dano de {fator}![/]")


class Guerreiro(Personagem):
    def __init__(self, nome, vida) -> None:
        super().__init__(nome, vida)
        self.golpes = ["Soco", "Golpe giratório", "Espadada Grossa", "Garoto"]

    def curar(self):
        fator = randint(0, 100)
        self.vida += fator
        print(f"[blue]{self.nome}[/]({self.vida}) enrolou uma atadura nos ferimentos e [green]recuperou {fator} pontos[/] de vida.")


class Mago(Personagem):
    def __init__(self, nome, vida) -> None:
        super().__init__(nome, vida)
        self.golpes = ["Poderzinho", "Varada", "A vara que raba", "Nós que know"]

    def curar(self):
        fator = randint(0, 100)
        self.vida += fator
        print(f"[blue]{self.nome}[/]({self.vida}) fez uma magia de cura e [green]recuperou {fator} pontos[/] de vida.")