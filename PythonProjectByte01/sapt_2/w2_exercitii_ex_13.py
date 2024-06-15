# 13. Printeaza dictionarul folosind stringuri formatate cu urmatoarea structura:
#	f”Trebuie cumparate 2 mere”
#	f”Trebuie cumparata 1 paine”

lista_cumparaturi = {'ulei': 6, 'zahar': 2, 'paine': 3, 'faina': 1, 'apa': 10, 'portocale': 2, 'banane': 4}

print(f'Trebuie cumparate {lista_cumparaturi.get('ulei')} sticle de {'ulei'}, {2} pungi de {'zahar'}, {3} bucati de {'paine'}')
