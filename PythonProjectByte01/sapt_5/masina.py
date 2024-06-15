# 4.Executa acealeasi 3 exercitii pentru clasa dreptunghi și pentru clasa masina

class Masina():
    # atributele unei masini, valorile sunt orientative
    cai_putere = 150
    capacitate_motor = 1900
    tip_caroserie = 'berlina'
    numar_inmatriculare = 'MM95DGF'
    an_fabricatie = 2003
    marca = 'VW'
    model = 'Golf'

    # constructor explicit
    def __init__(self, marca, model, an):
        self.marca = marca
        self.model = model
        self.an_fabricatie = an

    # celelalte metode de clasa
    def accelereaza(self):
        print(f'Masina {self.model} accelereaza!')

    def franeaza(self):
        print(f'Masina {self.model} franeaza!')
