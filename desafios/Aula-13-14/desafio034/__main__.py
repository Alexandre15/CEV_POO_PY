from classes import *


def main():
    f1 = Desenvolvedor("Alexandre", 3000)
    f2 = Designer("Alexandre2", 3000)
    f3 = Gerente("Alexandre3", 3000)

    print(f1)
    print(f1.calcular_bonus())

    print(f2)
    print(f2.calcular_bonus())

    print(f3)
    print(f3.calcular_bonus())

    f3.salario = 20
if __name__ == "__main__":
    main()