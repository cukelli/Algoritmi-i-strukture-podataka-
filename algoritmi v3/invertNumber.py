string = "Ovo je string"
brojac = 0
lista = []

for i in string:
    if (i == 'a') or (i == 'e') or (i == 'i') or (i == 'o') or (i == 'u'):
        lista.append(i)
        brojac += 1


print(set(lista))
print("Broj ponavljanja je", brojac)
