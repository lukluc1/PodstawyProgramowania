slowo = 'konstantynopolitanczykiewiczowianeczka'
samogloski = ['a', 'e', 'i', 'o', 'u', 'y']
slowo2 = ''.join([x for x in list(slowo)if not x in samogloski])
print(slowo2)

#zad 3
liczby = ['123', '56', '7890', '59', '456', '822']
lista_liczb = list(map(int, liczby))
print(sum(lista_liczb))

#zad 4
suma = 0
lista2d = [[4, 9, 2, 1, 7], [11, 2, 5, 6, 1],[8, 4, 1, 3, 5], [12, 9, 7, 23, 0], [1, 2, 3, 4, 5]]
for i in range(len(lista2d)):
    element = lista2d[i][i]
    suma += element
print(suma)

