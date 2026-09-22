from rich import print


class Diario:
    def __init__(self, senha = "retro") -> None:
        self.__segredos = []
        self.__senha = senha.strip()

    @property
    def senha(self):
        raise PermissionError("você não tem acesso a essa senha")
        
    def escrever(self, msg):
        if isinstance(msg, str) and len(msg) > 0:
            self.__segredos.append(msg.strip())

    def ler(self, password):
        if password == self.__senha:
            print("[green]DIARIO LIBERADO[/]")
            for msg in self.__segredos:
                print(f"-- {msg}")
        else:
            raise PermissionError("A senha está incorreta!")