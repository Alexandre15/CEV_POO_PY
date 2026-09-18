from classes import Aluno, Funcionario, Professor
from rich import inspect


def main():

    a1 = Aluno("Alexandre", 25, "Engenharia da Computação", "T01")
    a1.fazer_aniversario()
    a1.fazer_matricula()
    a1.estudar()
    # inspect(a1, methods=True)

    p1 = Professor("Guanabara", 48, "Programação", "Mestrado")
    p1.fazer_aniversario()
    p1.dar_aula()
    p1.estudar()
    # inspect(p1, methods=True)

    f1 = Funcionario("Vitoria", 22, "Handler I", "Logística")
    f1.fazer_aniversario()
    f1.bater_ponto()
    f1.estudar()
    # inspect(p1, methods=True)


if __name__ == "__main__":
    main()