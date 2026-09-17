class ContaBancaria:
    """=========================================================
    Cria uma conta bancária e permitefazer saques e depósitos
    =========================================================
    """

    def __init__(self, id, nome, saldo) -> None:
        self.id = id
        self.titular = nome
        self.saldo = saldo
        print(f"Conta {self.id} criada com sucesso. Saldo atual de R${self.saldo:,.2f}")


    def __str__(self) -> str:
        return f"\033[1;32mA conta {self.id} de {self.titular} tem R${self.saldo:,.2f} de saldo\033[m"


    def depositar(self, valor):
        self.saldo += valor
        print(f"\033[96mDepósito no valor de:\033[m \033[1;32m+R${valor:,.2f}\033[m \033[96mautorizado na conta {self.id}\033[m")


    def sacar(self, valor):
        if self.saldo < valor:
            print("Saldo insuficiente.")
        else:
            self.saldo -= valor
            print(f"\033[96mSaque no valor de:\033[m \033[1;31m-R${valor:,.2f}\033[m \033[96mautorizado na conta {self.id}\033[m")




c1 = ContaBancaria(115, "Alexandre", 3000)
print(c1)
c1.depositar(2456.32)
print(c1)
c1.sacar(1440.16)
print(c1)
c1.sacar(5000)
print(c1)