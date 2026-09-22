from classes029 import *
from rich import inspect


def main():
    diario = Diario("Gafanhoto")

    diario.escrever("Olá, Mundo!")
    diario.escrever("Vanderson cuzão!")

    #inspect(diario, private=True, methods=True)
    try:
        diario.ler("Gafanhoto")
    except Exception as e:
        print(f"[red]ERRO: {e}[/]")
if __name__ == "__main__":
    main()
