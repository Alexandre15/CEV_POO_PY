from classes import *


def main():
    u = [
        Usuario("Alexandre", "alefagundes155@gmail.com"),
        Usuario("Alexandre", "alex@gmail.com")
    ]

    a = [
        Aluno("Cláudia", "ADS", "2 per"),
        Aluno("Vitória", "ADM", "4 per"),
        Aluno("Mario", "SEG", "1 per")
    ]

    exportar_dados(JSON(), u)

if __name__ == "__main__":
    main()
