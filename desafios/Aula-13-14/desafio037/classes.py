from rich import print
from rich.panel import Panel


class Mensagem:
    icone = 'thought_balloon'
    def __init__(self, msg: str) -> None:
        self._mensagem = msg
        self._tipo = ""
        self._icone = self.icone

    def mostrar(self):
        match self.__class__.__name__:
            case "Alerta":
                self._tipo = "Alerta"
                estilo = "black on yellow"

            case "Mensagem":
                self._tipo = "AVISO"
                estilo = "white on black"

            case "Erro":
                self._tipo = "ERRO"
                estilo = 'yellow on red'
        panel = Panel(f"{self._mensagem}", title=f":{self._icone}: {self._tipo} :{self._icone}:", width=50, style=estilo)
        print(panel)


class Erro(Mensagem):
    icone = 'no_entry_sign'
    def __init__(self, msg: str) -> None:
        super().__init__(msg)
        self._icone = self.icone


class Alerta(Mensagem):
    icone = 'warning'
    def __init__(self, msg: str) -> None:
        super().__init__(msg)
        self._icone = self.icone

