class Pessoa:
    def __init__(self, nome = "", idade = 0):
        self.nome = nome
        self.idade = idade

    def fazer_aniversario(self):
        self.idade += 1


class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma) -> None:
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self):
        print(f"O Aluno {self.nome} acabou de fazer a matrícula.")


class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel) -> None:
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def dar_aula(self):
        print(f"O Professor(a) {self.nome} começou a dar aula.")
        

class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor) -> None:
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def bater_ponto(self):
        print(f"{self.nome} acabou de bater o ponto.")
