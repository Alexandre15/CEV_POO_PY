from avaliacao import *
from rich import inspect


def main():
    av1 = Avaliacao("Alexandre", "Engenharia da computação")
    av1.nota = -7.2
    inspect(av1, private=True)

if __name__ == "__main__":
    main()