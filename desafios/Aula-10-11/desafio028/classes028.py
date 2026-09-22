class Termostato:
    def __init__(self) -> None:
        self.__temperatura = 24

    @property
    def temperatura(self):
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, temp):
        if temp % 0.5 != 0:
            raise ValueError(f"Temperatura de {temp} é inválida!")
        elif temp <= 16:
            self.__temperatura = 16
        elif temp >= 30:
            self.__temperatura = 30
        else:
            self.__temperatura = temp


    @temperatura.getter
    def temperatura(self):
        return self.__temperatura

    @temperatura.getter
    def ftemperatura(self):
        return f"{self.__temperatura}ºC"