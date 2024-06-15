from forma import Forma

class Triunghi(Forma):
    culoare = 'culoare'
    latura = 5
    unghi = 45

    def __init__(self, culoare, latura, unghi):
        self.culoare = culoare
        self.latura = latura
        self.unghi = unghi


    def schimba_culoarea(self, culoare):
        self.culoare = culoare
        print(f'Triunghiul are culoarea {self.culoare}, latura de {self.latura} si unghiul de {self.unghi}')
