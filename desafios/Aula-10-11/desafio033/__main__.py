from classes033 import *
from rich import inspect


def main():
    a1 = Aluno("Vitoria", 2000, "ADS")

    a1.add_curso("MODA")

    print(a1.__dict__)

    inspect(a1, private=True, methods=True)

if __name__ == "__main__":
    main()