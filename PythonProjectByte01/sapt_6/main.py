from cerc import Cerc
from dreptunghi import Dreptunghi
from triunghi import Triunghi

cerc = Cerc('rosu', 5)
dreptunghi = Dreptunghi('albastru', 5, 3)
triunghi = Triunghi('negru', 10, 45)

cerc.schimba_culoarea('verde')
dreptunghi.schimba_culoarea('galben')
triunghi.schimba_culoarea('gri')

#print(cerc.__raza, cerc.culoare) odata ce raza este un atribut privat nu poate fi folosit in afara clasei
# print(dreptunghi.latime, dreptunghi.lungime, dreptunghi._grosime)
# putem accesa valorile atributelor protejate din afara clasei desi nu este recomandat; solutia este setter si getter
