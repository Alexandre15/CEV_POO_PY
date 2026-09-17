from time import sleep
from rich import print


pagina_atual = 2
class Livro:
    def __init__(self, titulo, paginas) -> None:
        self.titulo = titulo
        self.paginas = paginas
        self.pagina_atual = 1
        print(f":open_book: [blue]Você acabou de abrir o livro '[red]{self.titulo}[/]' que tem [green]{self.paginas} páginas[/] no total. Você está agora na [yellow] página 1[/]")


    def avancar_paginas(self, pag):
        cont = 0
        while True:
        
            if self.pagina_atual < self.paginas and cont < pag:
                cont += 1
                self.pagina_atual += 1
                print(f"Pág{self.pagina_atual} :arrow_forward: ", end="")
                sleep(.5)
            else:
                break

        print(f"[blue]Você avançou {cont} páginas e agora está na [yellow]página {self.pagina_atual}")
        
        if self.pagina_atual == self.paginas:
            print(f":closed_book: [red]Você chegou ao final do livro '{self.titulo}'")
            


l1 = Livro("O Princípe", 20)
l1.avancar_paginas(20)
# l1.avancar_paginas(100)
