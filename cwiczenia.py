from math import inf
#petle czesc 1
#zad 1
'''total = 0
for i in range(1, 20):
    if i % 5 == 0:
        continue
    total += i
    if total > 100:
        print(f'Suma przekroczyla 100 przy liczbie {i}')
        break
print(f'Końcowa summa to: {total}')

#zad 3


liczba = int(input('podaj liczbe calkowita dodatnia'))
liczek = 0
for x in range (1, liczba + 1):
    if liczba % x == 0 and x % 2 == 0:
        liczek += 1
print(liczek)

# zad 4

for y in range(100, 1001):
    if y % 11 == 0:
        print(y, end=", ")



#zad 5













#zad 6


zad = (20, 1)
for z in zad:
    if z % 3 == 0:
        print('fizz')
    elif z % 5 == 0:
        print('buzz')
    else:
        print('zadne')


#zad 7

qwer = (1, 51)
for u in range(len(qwer)):
    if not u % 2 == 0 or not u % 3 == 0:
        print(u, end= ", ")'''

'''lista = [12, 48, 78, 101, 9, -5, 9, 7, 23]
for x in lista:
    if x % 2 != 0:
        print(x)

g = int(input('Podaj liczbę'))
while g != 0:
    print(g)
    g = int(input('Podaj liczbę'))'''


napis = ('informatyka')
for x in range(5):
    print(napis)

ilosc = [1, 2, 3, 4, 5]
for x in range(len(ilosc)):
    print(napis)

lista = [34, 90, 77, 56, 54, 33, 21, 98, 45]
for i in lista:
    if i % 3 == 0:
        print(i)

xd = []
k = 1
while True:
    xd.append(k)
    k += 1
