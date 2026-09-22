from rich import inspect
from classes031 import *


def main():
    r = Retangulo()

    r.base = 12
    r.altura = 33
    #r.medidas = (9, 3)

    inspect(r, private=True, methods=True)
    print(r.medidas)

if __name__ == "__main__":
    main()