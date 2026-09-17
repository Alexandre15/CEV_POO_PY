from rich import print
from rich.panel import Panel


class Churrasco:
    def __init__(self, titulo="churrasco", quantidade=10) -> None:
        self.titulo = titulo
        self.quantidade = quantidade


    def analisar(self):
        # CONSIDERE
        # Consumo padrão: 400g por pessoa
        # Preço: R$82,40/Kg
        QuilosTotais = 0.4 * self.quantidade
        ValorTotal = QuilosTotais * 82.40
        ValorDividido = ValorTotal / self.quantidade

        painel = Panel(
        f"Analisando [green]{self.titulo}[/] com [blue]{self.quantidade} convidados[/]\nCada participante comerá 0.4Kg r cada Kg custa R$82.40\nRecomendo [blue]comprar {QuilosTotais:.2f}Kg[/] de carne\nO custo total será de [green]R${ValorTotal:,.2f}\nCada pessoa pagará [yellow]R${ValorDividido:,.2f}[/]",
        title=f"{self.titulo}",
        width=60
        )
        return painel


c1 = Churrasco("Churrasco dos Guri", 3)
print(c1.analisar())