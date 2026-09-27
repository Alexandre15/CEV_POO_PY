from abc import ABC
from datetime import date


class Pessoa(ABC):
    def __init__(self, nome, nascimento) -> None:
        super().__init__()
        self._nome = nome
        self._nascimento = None
        self.nascimento = nascimento

    @property
    def nascimento(self):
        return self._nascimento

    @nascimento.setter
    def nascimento(self, ano):
        if 1900 <= ano <= date.today().year:
            self._nascimento = ano
        else:
            raise ValueError(f"Ano {ano} é [red]Inválido[/]")

    @property
    def idade(self):
        return date.today().year - self._nascimento

    @idade.setter
    def idade(self):
        raise PermissionError("Você não pode alterar a idade. Mude o ano de nascimento.")


class Aluno(Pessoa):
    
    cursos_oficiais = ['ADM',  'ADS', 'ENG', 'CONT']

    def __init__(self, nome:str, nascimento:int, curso:str) -> None:
        super().__init__(nome, nascimento)
        self._curso = None
        self.curso = curso

    @property
    def curso(self):
        return self._curso

    @curso.setter
    def curso(self, curso):
        if curso in Aluno.cursos_oficiais:
            self._curso = curso
        else:
            self._curso = None
            raise ValueError(f"O curso {curso} não está na lista de cursos oficiais.")

    def add_curso(self, curso:str):
        curso = curso.strip().upper()

        if 3 <= len(curso) <= 5:
            if curso in Aluno.cursos_oficiais:
                raise ValueError("Já existe o curso na lista.")
            else:
                Aluno.cursos_oficiais.append(curso)
        else:
            raise ValueError(f"Nome {curso} está fora do padrão para Cursos!")