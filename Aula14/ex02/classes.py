class Carteira:

    def __init__(self, valor: float = 0) -> None:
        self.__saldo = valor

    def __str__(self) -> str:
        return f"Você tem R${self.saldo:,.2f} na carteira."

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        raise PermissionError("Você não tem autorização para alterar o saldo desse jeito.")

    def __eq__(self, outro: object) -> bool:
        if not isinstance(outro, Carteira):
            return NotImplemented
        return self.__saldo == outro.__saldo

    def __iadd__(self, valor: float):
        self.__saldo += valor
        return self

    def __isub__(self, valor: float):
        self.__saldo -= valor
        return self