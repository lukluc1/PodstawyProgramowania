#jak nie programować wielokrotnie powtarzalnych czynności

'''a = float(input('Podaj liczbe'))
b = float(input('Podaj liczbe'))
c = float(input('Podaj liczbe'))
d = float(input('Podaj liczbe'))
e = float(input('Podaj liczbe'))

suma = (a + b + c + d + e)

print(suma)'''
from glob import translate

'''liczba = 0
suma = 0

for i in range (5):
    liczba = float(input('Podaj liczbe'))
    suma = suma + liczba

print(suma)

#1. Listy
lista = ['qwerty', 56, [6, 7], 4.56, [[5, 8], 1]]
print(lista[2][1])
print(lista[4][0][1])

#2. listy i petle
lista2 = ['kot', 'pies', 'owca', 'lama']

#Pętla for:
#-> wyciąga dane z listy (jedna po drogiej)
#-> wykonuje sie tyle razy ile elementów ma lista
for z in lista2:
    print(z)

#Petla ktora wykona sie 3 razy
lista3 = [1414, 15, 7]

for i in lista3:
    print('OK')

#Petla ktoar wykonuje sie 1000 razy
lista4 = [[0] * 10 for i in range(10)]
print(lista4)
lista4 = [0] * 10
for i in lista4:
    print('cześć')

#3. Generatory i pentle
przedzial = range(1, 10) #{1, 2, 3, 4, 5, 6, 7, 8, 9}

for i in przedzial:
    print(i)

#Petla ktora wykona sie 10 razy
for i in range(10): #range(1, 10), 10 - liczba powtorzen
    print(i)'''

'''lista5 = [0]
lista5.append(0)
print(lista5)'''

lista = [0]

'''for i in lista:
    print('cześć')
    lista.append(0)'''

#4. Petle while

liczba = 5

while liczba > 0:
    print(liczba)
    liczba = liczba - 1