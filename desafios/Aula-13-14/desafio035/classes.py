from abc import ABC, abstractmethod


class Arquivo(ABC):
    def __init__(self, nome: str, ext:str, tamanho: int = 0) -> None:
        super().__init__()
        self.nome = nome
        self.tamanho = tamanho
        self._extensao = None
        self.extensao = ext

    @property
    def nome_completo(self):
        return f"'{self.nome}.{self._extensao}'({self.tamanho/1_000_000:.2f}MB)"

    @property
    def extensao(self):
        return self._extensao

    @extensao.setter
    def extensao(self, ext:str):
        formatos = ['pdf', 'docx']
        ext = ext.lower().strip()
        if ext in formatos:
            self._extensao = ext
        else:
            raise AttributeError("O arquivo está em um formato não suportado.")

    @abstractmethod
    def abrir(self):
        pass


class PDF(Arquivo):
    def __init__(self, nome: str = "", tamanho: int = 0) -> None:
        super().__init__(nome, 'pdf', tamanho)

    def abrir(self):
        print(f"Abrindo o arquivo {self.nome_completo} no Adobe Reader.")


class DOC(Arquivo):
    def __init__(self, nome: str = "", tamanho: int = 0) -> None:
        super().__init__(nome, 'docx', tamanho)

    def abrir(self):
        print(f"Abrindo o arquivo {self.nome_completo} no Microsoft Word.")


def abrir_arquivo(obj):
    if isinstance(obj, Arquivo):
        obj.abrir()
