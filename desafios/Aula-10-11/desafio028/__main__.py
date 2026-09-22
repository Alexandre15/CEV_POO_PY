from classes028 import *
from rich import print


def main():

    t1 = Termostato()

    t1.temperatura = 25.5

    print(f"A temperatura atual é [blue]{t1.ftemperatura}[/]")

if __name__ == "__main__":
    main()