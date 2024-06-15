# 2. Scrieti un program care sa parcurga un string și sa returneze o lista cu pozitiile la care se afla
# litera ‘a’ in acel string.

fraza = input('Introduceti un text: ')
pozitii_a = []
for i in range(len(fraza)):
    if fraza[i] == 'a' or fraza[i] == 'A':
        pozitii_a.append(i)

print(pozitii_a)
