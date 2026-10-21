class Carrinho:
    def __init__(self, produtos: list | None = None):
        self.produtos = produtos if produtos else []

    def __add__(self, outro):
        if isinstance(outro, Produto):
            return Carrinho(self.produtos + [outro])
        elif isinstance(outro, Carrinho):
            return Carrinho(self.produtos + outro.produtos)
        else:
            raise TypeError("Você tentou adicionar algo inválido ao carrinho.")

    @property
    def total(self):
        return sum(p.preco for p in self.produtos)

    def __str__(self):
        linha = "\n" + "-=" * 15 + "\n"
        itens = "\n".join(str(p) for p in self.produtos)
        return f"{itens} {linha}Total: {fdinheiro(self.total)}\n"



class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self) -> str:
        return f"{self.nome} ({fdinheiro(self.preco)})"


def fdinheiro(valor: float):
    import locale
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    return locale.currency(valor, grouping=True)