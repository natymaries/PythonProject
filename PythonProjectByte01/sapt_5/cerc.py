# 1.Modeleaza clasa Cerc cu atribute și metode (constructor, setters, getters și deleters)
# 2.Implementeaza clasa Cerc intr-un fisier python

class Cerc():
    raza_cercului = 7

    def __init__(self, raza_cercului):
        if raza_cercului > 0:
            self.raza_cercului = raza_cercului
        else:
            print('Ati introdus o raza invalida!')

    def get_raza(self):
        return self.raza_cercului

    def set_raza(self, raza):
        if raza > 0:
            self.raza_cercului = raza
        else:
            raise ValueError('Raza trebuie sa fie un numar pozitiv')

    def del_raza(self):
        # del self.raza_cercului - # instructiunea del reseteaza valoarea initiala a atributului

        self.raza_cercului = None # - asignam None (non valoarea) a atributului raza_cercului



