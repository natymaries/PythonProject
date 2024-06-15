# 3.Creaza un nou fisier python, importeaza clasa Cerc, creaza cateva cercuri și apeleaza metodele
from cerc import Cerc
from masina import Masina
from dreptunghi import Dreptunghi

cerc_1 = Cerc(5)
raza = cerc_1.get_raza()
print(raza)

cerc_2 = Cerc(7)
cerc_2.set_raza(5)
# cerc_2.del_raza()
print(cerc_2.get_raza())
cerc_3 = Cerc(-4)
cerc_3.set_raza(4)
print(cerc_3.get_raza())

masina_servici = Masina('VW', 'polo', '2020')
masina_servici.accelereaza()
masina_servici.franeaza()

dreptunghi = Dreptunghi(8, 5)
aria_dreptunghi.aria()
perimetru_dreptunghi.perimetru()
