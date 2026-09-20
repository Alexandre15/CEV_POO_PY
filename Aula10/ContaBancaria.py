class ContaBancaria:
    """=========================================================
    Cria uma conta bancária e permitefazer saques e depósitos
    =========================================================
    """

    def __init__(self, id, nome, saldo) -> None:
        self.id = id # público (+)
        self._titular = nome # protegido (#)
        self.__saldo = saldo # privado (-)
        print(f"Conta {self.id} criada com sucesso. Saldo atual de R${self.__saldo:,.2f}")


    def __str__(self) -> str:
        return f"Estado atual da conta: {self.__dict__}"


    def depositar(self, valor):
        valor = abs(valor)
        self.__saldo += valor
        print(f"\033[96mDepósito no valor de:\033[m \033[1;32m+R${valor:,.2f}\033[m \033[96mautorizado na conta {self.id}\033[m")


    def sacar(self, valor):
        valor = abs(valor)
        if self.__saldo < valor:
            print("Saldo insuficiente.")
        else:
            self.__saldo -= valor
            print(f"\033[96mSaque no valor de:\033[m \033[1;31m-R${valor:,.2f}\033[m \033[96mautorizado na conta {self.id}\033[m")
