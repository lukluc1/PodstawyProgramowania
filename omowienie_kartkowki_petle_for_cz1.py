'''lista = [12, 45, 78, 101, 9, -5, 9, 7, 23]'''

#zadanie 2 gr b
#sposob 1
'''for i in range(len(lista)):
    if i % 2 == 1:
        print(lista[i])'''

#sposob 2
'''for i in range(1, len(lista), 2):
    print(lista[i])
'''
#sposob 3
'''for i in lista[1::2]:
    print(i)'''

#sposob 4
'''i = 1
while i < len(lista)
    print(lista[i])
    i = i + 2'''
    #1 += 2

#zadanie 4
lista3 = [100]

for x in lista3:
    liczba = float(input('Podaj liczbę'))
    print(liczba)
    if liczba != 0:
        lista3.append([])
