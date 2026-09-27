from rich import print


class Porta:
    def abrir(self):
        print("[bold dark_goldenrod on white]PORTA[/]: Girar a maçaneta e empurrar/puxar a porta.")


class Empresa:
    def abrir(self):
        print("[bold blue on white]EMPRENDEDOR[/]: Vá ao portal do empreendedor com toda a documentação para abrir um CNPJ.")


class Ovo:
    def abrir(self):
        print("[bold yellow on white] OVO [/]: Quebre a casca com um garfo e separe as partes sobre uma frigideira.")


class Pedra:
    pass


# METODO PYTHONICO POLIMORFICO DUCK TYPING

def tentar_abrir(objeto):
    try:
        objeto.abrir()
    except:
        print(f"Encontrei problemas ao tentar abrir um objeto tipo [blue]{objeto.__class__.__name__}[/]")