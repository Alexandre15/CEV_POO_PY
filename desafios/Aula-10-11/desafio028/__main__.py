from classes028 import *
from rich import print


def main():

    t1 = Termostato()
    try:
        t1.temperatura = 25.2

    except Exception as erro:
        print(f"Houve um problema: {erro}")

    print(f"A temperatura atual é [blue]{t1.ftemperatura}[/]")

if __name__ == "__main__":
    main()