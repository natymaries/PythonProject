# 8. Adauga și zilele de weekend și apoi printeaza setul

zile_lucratoare = {'luni', 'marti', 'miercuri', 'joi', 'vineri'}
zile_weekend = {'sambata','duminica'}
zile_totale = zile_lucratoare.union(zile_weekend)

print(zile_totale)