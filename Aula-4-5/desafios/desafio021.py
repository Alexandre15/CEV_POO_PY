from rich import print


class Caneta:
    def __init__(self, cor) -> None:
        self.cordacaneta = ""
        self.tampa = False
        match cor.lower().strip():
            case "vermelha":
                self.cordacaneta = "[red]"
            case "verde":
                self.cordacaneta = "[green]"
            case "azul":
                self.cordacaneta = "[blue]"
        # print(f"A cor da caneta é {self.cordacaneta}")


    def quebra_linha(self, quebras):
        print("\n"*(quebras-1))


    def destampar(self):
        if self.destampar:
            self.tampa = True


    def escrever(self, texto):
        if self.tampa == True:
            print(f"{self.cordacaneta}{texto}")
        else:
            print(f":no_entry_sign: A {self.cordacaneta}Caneta[/] está tampada")


c1 = Caneta("Azul")
c2 = Caneta("Verde")
c3 = Caneta("Vermelha")

c1.destampar()
c2.destampar()
#c3.destampar()

c1.quebra_linha(1)

c1.escrever("Olá Mundo!")
c2.escrever("Olá, Gafanhoto")
c3.escrever("Olá, tudo bem?")
