class Elev():
    nume = 'nume'
    varsta = 14
    inaltime = 1.75
    clasa = 7
    medie_note = 8.45

    def __init__(self, nume, varsta, inaltime, clasa, medie_note):
        self.nume = nume
        self.varsta = varsta
        self.inaltime = inaltime
        self.clasa = clasa
        self.medie_note = medie_note

    def schimba_varsta(self, varsta):
        self.varsta = varsta
        print(f'Ai varsta de {varsta} ani')

    def absolva(self, medie_note):
        if medie_note >= 5.0:
            print(f'Felicitari! Ai obtinut media {medie_note}')
        else:
            print(f'Ai obtinut media {medie_note}. Mai incearca')