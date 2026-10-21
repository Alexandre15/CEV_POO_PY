from abc import ABC, abstractmethod


class Funcionario(ABC):
    def __init__(self, nome: str | None = None, sal: float = 1621) -> None:
        super().__init__()
        self.nome = nome
        self.__salario = sal

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, val: float | None = None):
        if val is None:
            raise ValueError("Impossível reajustar o salário desse jeito!")
        else:
            if val >= self.__salario:
                self.__salario = val      
            else:
                raise ValueError("Você não pode diminuir o salário, senão vira bagunça né filhão!")

    @salario.getter
    def salario(self):
        return self.__salario

    @abstractmethod
    def calcular_bonus(self):
        return f"Salário {self.salario}, Bonus de 50% {self.salario * 90/100}"

    def __str__(self) -> str:
        return f"{self.nome} ganha R${self.salario:,.2f} e por ser {self.__class__.__name__} o bônus será de R${self.calcular_bonus():,.2f}"


class Gerente(Funcionario):
    # ===========
    #     15%
    # ===========
    bonus = 15
    def __init__(self, nome, sal):
        super().__init__(nome, sal)

    def calcular_bonus(self):
        return self.salario * Gerente.bonus/100


class Designer(Funcionario):
    # ===========
    #     8%
    # ===========
    bonus = 8
    def __init__(self, nome, sal):
        super().__init__(nome, sal)

    def calcular_bonus(self):
        return self.salario * Designer.bonus/100


class Desenvolvedor(Funcionario):
    # ===========
    #     10%
    # ===========
    bonus = 10
    def __init__(self, nome, sal):
        super().__init__(nome, sal)

    def calcular_bonus(self):
        return self.salario * Desenvolvedor.bonus/100
