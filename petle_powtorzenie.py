lista = [10, 56, 89, 59]

#1. chodzenie bezposrednio po elementach listy
#do zmiennej b trafiaja bezposrednio elementy listy, tzn. 10, 56, 89, 59
'''for b in lista:
    print(b)
'''
#2. chodzenie po liscie z uzyciem indeksów
#2.1 co to jest indeks?
# lista[2]
# 2 - indeks
# lista [2] - element znajdujacy sie pod indeksem 2 = 56

#2.2.
for k in range(len(lista)): #range(0, 4)
    print(lista[k])