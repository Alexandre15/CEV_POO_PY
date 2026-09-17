# Declaração de Clase

class Gafanhoto:
    def __init__(self) -> None: # Metodo construtor
        # Atributos de Instância
        self.nome = ""
        self.idade = 0

    # Metodos de Instância
    def aniversario(self):
        self.idade += 1


    def mensagem(self):
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade."

# Declaração de Objetos
gafanhoto1 = Gafanhoto()
gafanhoto1.nome = "Alexandre"
gafanhoto1.idade = 25
gafanhoto1.aniversario()
print(gafanhoto1.mensagem())

gafanhoto2 = Gafanhoto()
gafanhoto2.nome = "Vitória"
gafanhoto2.idade = 22
gafanhoto2.aniversario()
print(gafanhoto2.mensagem())
