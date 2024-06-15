#Tuplu de coordonate GPS:
coordonate = (40.7128, -74.0060)
print(coordonate)
print(type(coordonate))
#Tuplu de informații despre un angajat:
angajat = ("John", 30, "Manager")
i_30 = angajat.index(30)
print(i_30)
print(angajat[1])

#Tuplu de cifre norocoase:
cifre_norocoase = (7, 13, 21, 42)

#Tuplu de numere complexe:
numere_complexe = ((1, 2), (3, 4), (5, 6))

tuplu = (1, 2, 3, 2, 4)
print(tuplu.count(4))

#Returnează indexul primei apariții a unui element în tuplu.
index = tuplu.index(2)
#Numără de câte ori apare un element în tuplu.
cate = tuplu.count(2)
#Returnează lungimea (numărul de elemente) a unui tuplu.
lungime = len(tuplu)
#Returnează un tuplu nou cu tuplurile concatenate
tuplu_concatenat = tuplu + numere_complexe
print(tuplu_concatenat)
# printeaza tipul de date al ultimului element al tuplului concatenat
prinprint(type(tuplu_concatenat[-1]))
