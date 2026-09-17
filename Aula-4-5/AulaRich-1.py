from rich import print  # rich.readthedocs.io  <- Site com a documentação do rich
from rich.panel import Panel

print("\n")

caixa = Panel("[white]Esse aqui é um painel de exemplo[/]:+1:", title="Mensagem", style="red", width=40)

print(caixa)


print("\n")
print("=-"*88)
print("\n")

print("Olá [red]Mundo![/red]:earth_americas:")
print("Olá, [bold blue on white]Pequeno Gafanhoto[/] :vulcan_salute: :moai:")
print(":+1: :martial_arts_uniform: :-1:")
