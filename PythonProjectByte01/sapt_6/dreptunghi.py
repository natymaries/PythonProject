from forma import Forma

class Dreptunghi(Forma):
    culoare = 'culoare'
    lungime = 2
    latime = 1
    _grosime = 0
    def __init__(self, culoare, lungime, latime):
        self.culoare = culoare
        if lungime > latime:
            self.lungime = lungime
            self.latime = latime
            self._grosime = 3
        else:
            print('Introduceti o lungime mai mare dacat latimea')

    def schimba_culoarea(self, culoare):
        self.culoare = culoare
        print(f'Dreptunghiul are culoarea {self.culoare} si grosimea {self._grosime}')

