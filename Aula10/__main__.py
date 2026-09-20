from ContaBancaria import *
from rich import print


def main():
    c1 = ContaBancaria(15, "Alexandre", 15458)
    c1.depositar(1000)
    print(c1)

if __name__ == "__main__":
    main()