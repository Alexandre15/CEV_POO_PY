from rich import print
from rich.table import Table
from transportes import *


def main():
    dist = 10

    entrega = Moto(dist)
    # print(f"Frete de {type(entrega).__name__} em {dist}Km = {entrega.calc_frete()}")

    entrega2 = Drone(dist)
    # print(f"Frete de {type(entrega2).__name__} em {dist}Km = {entrega2.calc_frete()}")

    entrega3 = Caminhao(dist)
    # print(f"Frete de {type(entrega3).__name__} em {dist}Km = {entrega3.calc_frete()}")

    tabela = Table()
    tabela.add_column("Distância")
    tabela.add_column("Tipo")
    tabela.add_column("Frete")

    tabela.add_row(f"{dist}Km", f"{type(entrega).__name__}", f"{entrega.calc_frete()}")
    tabela.add_row(f"{dist}Km", f"{type(entrega2).__name__}", f"{entrega2.calc_frete()}")
    tabela.add_row(f"{dist}Km", f"{type(entrega3).__name__}", f"{entrega3.calc_frete()}")

    print(tabela)

if __name__ == "__main__":
    main()