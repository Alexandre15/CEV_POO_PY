from Aula7Modulo import Aluno, Funcionario, Professor
from rich import inspect


def main():

    a1 = Aluno("Alexandre", 25, "Engenharia da Computação", "T01")
    a1.fazer_aniversario()
    a1.fazer_matricula()
    #inspect(a1, methods=True)

    p1 = Professor("Guanabara", 37, "Programação", "Mestrado")
    p1.fazer_aniversario()
    p1.dar_aula()
    #inspect(p1, methods=True)

    f1 = Funcionario("Vitoria", 22, "Handler I", "Logística")
    f1.fazer_aniversario()
    f1.bater_ponto()
    inspect(p1, methods=True)


if __name__ == "__main__":
    main()