dodawanie = lambda x, y: x + y
print(dodawanie(5, 6))

#I zaawansowane sortowanie
lista = [6, -9, 3, 0, -12, -1, 7]


#1) sortowanie po wartoscki bezwzglednej
lista.sort(key = lambda x: abs(x))
print(lista)

#2) sortowanie po dlugosciach napisow
lista2 = ['matematyka', 'filozofia', 'fizyka', 'informatyka']
lista2.sort(key = lambda x: len(x))
print(lista2)


#3) sortowanie wielopoziomowe
ludzie = [['Janusz', 'Baca'], ['Bartlomiej', 'Kaca'], ['Janusz', 'Aca'], ['Bartlomiej', 'Gaca']]
ludzie.sort(key = lambda x: (x[0], x[1]))
print(ludzie)


#4) sortowanie po liczbie dzielnikow
def ile_dzielnikow(liczba):
    ile = 0
    for x in range(1, liczba + 1):
        if liczba % x == 0:
            ile += 1
    return ile
lista3 = [12, 7, 1024, 9, 16]
lista3.sort(key = lambda x: ile_dzielnikow(x))
print(lista3)

#II Zawansowane uzycie funkcji map

#proste mapowanie
lista4 = [1, 5, -6, 10, -7]
kwadraty4 = list(map(lambda x: x**2,lista4))
print(kwadraty4)

#zaawansowane mapowanie
slownik = {'fiz': 'fizyka', 'mat': 'matematyka', 'inf': 'informatyka'}
lista5 = ['fiz', 'jest', 'najlepsza', 'ale', 'inf', 'tez', 'jednak', 'nic', 'nie', 'zastapi', 'mat']
lista6 = list(map(lambda x: slownik[x] if x in slownik else x, lista5))
print(lista6)