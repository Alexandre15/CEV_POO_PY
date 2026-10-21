from abc import ABC, abstractmethod
import re


class Validador(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def validar(self, valor: str):
        # r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[^A-Za-z0-9]).+"
        pass


# Usuário
# - de 5 a 20 caracteres
# - Letras minúsculas
# - Números
# - Símbolo de sublinhado
class Usuario(Validador):
    def __init__(self) -> None:
        super().__init__()

    def validar(self, valor: str) -> bool:
        regex = r"^[a-z0-9_]{5,20}$"
        return re.fullmatch(regex, valor) is not None



# E-mail
# - Deve conter uma única @
# - Usuário pode conter letras, números e alguns símbolos
# - Os domínios contém pontos
# - O TLD encerra com ponto e pelo menos 2 letras
class Email(Validador):
    def __init__(self) -> None:
        super().__init__()

    def validar(self, valor: str) -> bool:
        regex = r"^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z0-9]{2,}$"
        return re.fullmatch(regex, valor) is not None


# Senha
# - Pelo menos 8 caracteres
# - Pelo menos uma maiúscula
# - Pelo menos um símbolo
class Senha(Validador):
    def __init__(self) -> None:
        super().__init__()

    def validar(self, valor: str) -> bool:
        regex = r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[^A-Za-z0-9]).{8,}"
        return re.fullmatch(regex, valor) is not None


def validar_dado(metodo: Validador, valor: str):

    if metodo.validar(valor):
        print(f"Valor: {valor} é válido? SIM")
    else:
        print(f"Valor: {valor} é válido? NÃO")
    