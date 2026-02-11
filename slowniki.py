oceny = {'matematyka': 3, 'fizyka': 2, 'jezyk polski': 4}

#klucze: 'matematyka', 'fizyka', 'jezyk polski'
#wartosci: 3, 2, 4

#1 Dostawanie sie do wartosci pod danym kluczem
print(oceny['fizyka']) # pobieramy wartosc przypisana do klucza 'fizyka', czyli 2

#2 Modyfikacja wartosci pod danym kluczem
oceny['jezyk polski'] = 5
print(oceny['jezyk polski'])

#3 Dodawanie klucza do slownika
oceny['geografia'] = 6
print(oceny)

#4 sklejanie slownika z listy kluczy i z listy wartosci
klucze = ['Bitwa pod grunwaldem', 'chrzest polski', 'III Rozbior polski']
wartosci = [1410, 966, 1795]
slownik = {}
for i in range(len(klucze)):
#print(klucze[i], wartosci[i])
    slownik[klucze[i]] = wartosci[i]

slownik2 = dict(zip(klucze, wartosci))
print(slownik2)

slownik3 = dict(janusz = 23, alojzy = 99, bronislawa = 67)
print(slownik3)

#5 usuwanie klucza ze slownika
del oceny['fizyka']
print(oceny)

#6 chodzenie w petli po slowniku
for k in oceny:
    print(k)

for i in oceny.items():
    print(i)