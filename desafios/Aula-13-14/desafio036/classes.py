import locale
from abc import ABC, abstractmethod

# from babel.numbers import format_currency


class Pagamento(ABC):
    def __init__(self) -> None:
        super().__init__()
        self._valor = 0

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, valor: float):
        if valor > 0:
            self._valor = valor
        else:
            raise ValueError("O pagamento só pode ser efetuado para valores positivos.")

    @property
    def fvalor(self):
        # return format_currency(self._valor, 'BRL', locale='pt_BR')
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        return locale.currency(self._valor, grouping=True)

    @abstractmethod
    def pagar(self, valor: float):
        pass


class Boleto(Pagamento):
    def __init__(self) -> None:
        super().__init__()

    def pagar(self, valor: float):
        try:
            self.valor = valor
            return f"Pagamento CONFIRMADO de {self.fvalor} via Boleto."
        except ValueError as erro:
            return f"Falha no pagamento de {self.fvalor} via Boleto! ERRO: {erro}"


class Credito(Pagamento):
    def __init__(self) -> None:
        super().__init__()

    def pagar(self, valor: float):
        try:
            self.valor = valor
            return f"Pagamento CONFIRMADO de {self.fvalor} via Cartão de Crédito."
        except ValueError as erro:
            return f"Falha no pagamento de {self.fvalor} via Cartão de Crédito! ERRO: {erro}"


class PIX(Pagamento):
    def __init__(self) -> None:
        super().__init__()

    def pagar(self, valor: float):
        try:
            self.valor = valor
            return f"Pagamento CONFIRMADO de {self.fvalor} via PIX."
        except ValueError as erro:
            return f"Falha no pagamento de {self.fvalor} via PIX! ERRO: {erro}"
        

def finalizar_pagamento(tipo_pag: Pagamento, valor: float):
    print(tipo_pag.pagar(valor))