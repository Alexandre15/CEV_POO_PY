class Retangulo:
    def __init__(self, base = 1, altura = 1) -> None:
        self._base = base
        self._altura = altura
        self._area = None

    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, base):
        if base > 0:
            self._base = base
        else:
            raise ValueError("Valor deve ser maior que zero!")

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, altura):
        if altura > 0:
            self._altura = altura
        else:
            raise ValueError("Valor deve ser maior que zero!")
        
    @property
    def medidas(self):
        return self._base, self._altura

    @medidas.setter
    def medidas(self, medidas):
        print(f"M0{medidas[0]}")
        print(f"M1{medidas[1]}")
        if medidas[0] > 0 and medidas[1] > 0:
            self._base, self._altura = medidas
        else:
            raise ValueError("As medidas não podem conter valor menor ou igual a zero!")
        return self._area

    @medidas.getter
    def medidas(self):
        return f"Base {self.base} \nAltura = {self.altura} \nÁrea = {self.area}"

    @property
    def area(self):
        self._area = self._base * self._altura
        return self._area

    @area.setter
    def area(self):
        return TypeError
