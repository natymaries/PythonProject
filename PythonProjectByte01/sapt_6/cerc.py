from sapt_6.forma import Forma


class Cerc(Forma):
    culoare = 'culoare'
    __raza = 1
    def __init__(self, culoare, raza):
        self.culoare = culoare
        self.__raza = raza
    def schimba_culoarea(self, culoare):
        self.culoare = culoare
        print(f'Cercul este acum {self.culoare} si are raza {self.__raza}')