from classes032 import *
from rich import inspect, print


def main():
    #print("Criando a conta...")
    cc = ContaBancaria(15, "Alexandre", 900)
    print(cc)
    #print("Realizando depósito")
    #cc.depositar(1800.87)
    print("Realizando Saque")
    cc.sacar(800)
    #cc.nome = "Jão"
    
    #print(cc.validar_senha.__doc__)
    #print(cc.pede_senha.__doc__)
    #print(cc.sacar.__doc__)
    #print(cc.depositar.__doc__)

    #inspect(cc, private=True, methods=True)

if __name__ == "__main__":
    main()