from abc import ABC, abstractmethod

from rich import print
from rich.panel import Panel


class Funcionario(ABC):
    def __init__(self, nome) -> None:
        super().__init__()
        self.nome = nome
        self.sal_min = 1612
        self.inss = 7.5

    @abstractmethod
    def calc_sal(self) -> float:
        pass

    def analisar_sal(self):

        painel = Panel(f"O salário de [blue]{self.nome}[/] ([violet]{type(self).__name__}[/]) é de [green]R${self.calc_sal():,.2f}[/] e corresponde a [yellow]{self.calc_sal()/self.sal_min:.1f} salários mínimos", title="Análise de Salário", width=45)
        print(painel)

class Horista(Funcionario):
    def __init__(self, nome, valorh, horast) -> None:
        super().__init__(nome)
        self.valor_hora = valorh
        self.horas_trab = horast

    def calc_sal(self):
        calc_salario = self.valor_hora * self.horas_trab
        return calc_salario - (calc_salario * (self.inss / 100))

class Mensalista(Funcionario):
    def __init__(self, nome, sal_bruto) -> None:
        super().__init__(nome)
        self.sal_bruto = sal_bruto

    def calc_sal(self):
        return self.sal_bruto - (self.sal_bruto * (self.inss / 100))