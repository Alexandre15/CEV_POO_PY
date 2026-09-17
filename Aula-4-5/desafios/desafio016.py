from rich import print


class Funcionario:
    """Apresentação do Empregado
    """
    def __init__(self, nome, setor, cargo) -> None:
        self.nome = nome
        self.setor = setor
        self.cargo = cargo


    def apresentacao(self):
        return f":handshake: Olá, sou [blue]{self.nome}[/] e sou {self.cargo} do setor de {self.setor} da empresa Curso em Vídeo"


c1 = Funcionario("Alexandre", "Logística", "Expedidor")
print(c1.apresentacao())