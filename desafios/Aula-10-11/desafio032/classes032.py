from getpass import getpass
from hashlib import sha256


class ContaBancaria:
    def __init__(self, id:int, nome:str = "", saldo:float = 0, chave:str = "") -> None:
        self._id = id
        self._titular = nome
        self.__saldo = saldo
        if chave == "":
            self.__hash = sha256(self.pede_senha().encode('utf-8')).hexdigest().strip()
        else:
            self.__hash = sha256(chave.encode('utf-8')).hexdigest().strip()

    @property
    def nome(self):
        return self._titular

    @nome.setter
    def nome(self, nome):
        chave = self.pede_senha()
        if self.validar_senha(chave):
            self._titular = nome
            print(f"Nome alterado para {self._titular}")
        else:
            print("Não foi possível mudar o nome.")

    @nome.getter
    def nome(self):
        return self._titular

    # validar_senha(chave)
    def validar_senha(self, chave:str) -> bool:
        """
        [blue]VALIDAR A SENHA[/]

        Args:
            chave (str): Recebe a senha e verifica se está correta.

        Returns:
            boolean: Retorna Verdadeiro ou Falso
        """
        usuario = sha256(chave.encode('utf-8')).hexdigest().strip()
        return usuario == self.__hash

    # pede_senha()
    def pede_senha(self) -> str:
        """
        [blue]SOLICITA A SENHA[/]

        Returns:
            str: Retorna uma string, a digitação fica anônima.
        """
        while True:
            senha = str(getpass("Senha: ", echo_char="*")).strip()
            if len(senha) >= 6:
                break
        return senha
        
    # sacar(valor, senha)
    def sacar(self, valor, chave:str = ""):
        """
        [blue]SAQUE[/]

        Args:
            valor (float): Valor a ser depositado na conta
            chave (str, optional): chave para autorizar o saque, se não for adicionada na chamada da função é solicitado posteriormente. Defaults to "".
        """
        if len(chave) == 0:
            chave = self.pede_senha()

        if self.validar_senha(chave):
            if valor > self.__saldo:
                print(f"Saque [red]NEGADO[/] de R${valor:,.2f} na conta {self._id}")
            else:
                self.__saldo -= valor
                print(f"Saque de {valor} autorizado na conta {self._id}")

        else:
            print("Senha não confere. Saque não autorizado!")

    # depositar(valor)
    def depositar(self, valor):
        """
        [blue]DEPOSITAR[/]

        Args:
            valor (float): Função para deposito em conta.
        """
        self.__saldo += valor
        print(f"Depósito de R${valor:,.2f} autorizado na conta {self._id}")

    def __str__(self) -> str:
        return f"Estado atual da conta: {self.__dict__}"