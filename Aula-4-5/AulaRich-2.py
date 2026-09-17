from rich import print, inspect  # rich.readthedocs.io  <- Site com a documentação do rich
from rich.table import Table

tabela = Table(title="Tabela de Preços")

tabela.add_column("Nome", justify="left", style="red")
tabela.add_column("Preço", justify="center", style="blue")

tabela.add_row("Lápis", "R$1,50")
tabela.add_row("Borracha", "R$5,00")

print(tabela)

inspect(int, all=True)