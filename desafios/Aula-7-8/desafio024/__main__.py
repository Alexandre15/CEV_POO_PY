from cafeteria import *


def main():
    bebida = Cafe()
    bebida.preparar()

    bebida2 = Cha()
    bebida2.preparar()

    bebida3 = Leite()
    bebida3.preparar()

if __name__ == "__main__":
    main()