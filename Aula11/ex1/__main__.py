from Aula11.ex1.avaliacao import *
from rich import inspect


def main():
    av1 = Avaliacao("Alexandre", "Engenharia da computação", 9.5)
    av1.set_nota(-2.5)
    inspect(av1, private=True)

if __name__ == "__main__":
    main()