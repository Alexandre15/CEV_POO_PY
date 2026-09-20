from abc import ABC, abstractmethod

from rich import print
from rich.panel import Panel


class Funcionario(ABC):
    sal_min = 1612
    inss = 7.5
    def __init__(self, nome) -> None:
        super().__init__()
        self.nome = nome
        self.salario_bruto = 0
        self.salario = 0

    @abstractmethod
    def calc_sal(self) -> float:
        pass

    def analisar_sal(self):

        painel = Panel(f"O salário de [blue]{self.nome}[/] ([violet]{type(self).__name__}[/]) é de [green]R${self.calc_sal():,.2f}[/] e corresponde a [yellow]{self.salario/Funcionario.sal_min:.1f} salários mínimos", title="Análise de Salário", width=45)
        print(painel)
        print("\n")

class Horista(Funcionario):
    def __init__(self, nome, valorh = 7.37, horast = 220) -> None:
        super().__init__(nome)
        self.valor_hora = valorh
        self.horas_trab = horast
        self.salario_bruto = self.valor_hora * self.horas_trab

    def calc_sal(self):
        self.salario = self.salario_bruto - (self.salario_bruto * Funcionario.inss / 100)
        return self.salario

class Mensalista(Funcionario):
    def __init__(self, nome, sal_bruto) -> None:
        super().__init__(nome)
        self.sal_bruto = sal_bruto

    def calc_sal(self):
        self.salario = self.sal_bruto - (self.sal_bruto * (self.inss / 100))
        return self.salario