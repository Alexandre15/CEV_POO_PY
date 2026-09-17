# Declaração de Clase

class Gafanhoto:
    """===============================================================================
    \033[1;36mEssa classe cria um Gafanhoto, que é uma pessoa que tem nome e idade.\033[m

    \033[1;92mPara criar uma nova pessoa, use:\033[m
    \033[1;33m╚> \033[1;94mvariável = Gafanhoto(nome, idade)\033[m
    ===============================================================================
    """

    def __init__(self, nome = "vazio", idade = 0) -> None: # Metodo construtor
        # Atributos de Instância
        self.nome = nome
        self.idade = idade

    # Metodos de Instância
    def aniversario(self):
        self.idade += 1


    def mensagem(self):
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade."


    def __str__(self) -> str: # Dunder Method
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade."

    def __getstate__(self) -> object:
        return f"\033[1;36mEstado:\033[m\n\033[1;32m    nome: {self.nome}\n    idade = {self.idade}\033[m"


# Declaração de Objetos
gafanhoto1 = Gafanhoto("Alexandre", 25)
gafanhoto1.aniversario()

#print(gafanhoto1.__doc__)
#print(gafanhoto1)
print(gafanhoto1.__dict__)
print(gafanhoto1.__getstate__())
print(gafanhoto1.__class__)