from abc import ABC, abstractmethod


# ================================================================
#                       CLASSE MÃE (ABC)
# ================================================================
class Animal(ABC):
    def __init__(self, nome:str = "") -> None:
        super().__init__()
        self.nome = nome

    @abstractmethod
    def emitir_som(self):
        print(f"{self.nome} é {self.__class__.__name__} e está emitindo um som")

# ================================================================
#                       CLASSE PATO (ANIMAL)
# ================================================================
class Pato(Animal):
    def emitir_som(self):
        print(f"{self.nome} acabou de dizer QUACK! QUACK! QUACK!")

# ================================================================
#                       CLASSE CACHORRO (ANIMAL)
# ================================================================
class Cachorro(Animal):
    def emitir_som(self):
        print(f"{self.nome} acabou de dizer AU! AU! AU!")

class Spitz(Cachorro):
    def emitir_som(self):
        print(f"{self.nome} acabou de dizer au!au!au!au!au!au!")

class PitBull(Cachorro):
    def emitir_som(self):
        print(f"{self.nome} acabou de dizer RUF! RUF! RUF!")

# ================================================================
#                       CLASSE GATO (ANIMAL)
# ================================================================
class Gato(Animal):
    def emitir_som(self):
        print(f"{self.nome} acabou de dizer MIAU! MIAU! MIAU!")

# ================================================================
#                       CLASSE GALINHA (ANIMAL)
# ================================================================
class Galinha(Animal):
    def emitir_som(self):
        print(f"{self.nome} acabou de dizer PÓ! PÓ! PÓ!")