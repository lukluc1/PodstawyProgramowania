zbior = {5, 6, 6, 1, 1, 5, 9}
print(zbior)

zbior2 = {'kot', 'pies', 'gołąb', 'kot', 'pies'}
print(len(zbior2))

A = set(range(0, 20, 2))  #{0, 2, 4, 6, 8, 10, 12, 14, 16, 18,}
B = {1, 2, 3, 4, 6, 12}


# suma zbiorów
suma = A.union(B)    #{0, 2, 4, 6, 8, 10, 12, 14, 16, 18,} u {1, 2, 3, 4, 6, 12}
print(suma)
print(set(list(A) + list(B)))


#czesc wspolna (iloczyn)
iloczyn_a_b = A.intersection(B)  # {0, 2, 4, 6, 8, 10, 12, 14, 16, 18,} n {1, 2, 3, 4, 6, 12}
print(iloczyn_a_b)

#roznica
roznica_a_b = A.difference(B)   # {0, 2, 4, 6, 8, 10, 12, 14, 16, 18,} - {1, 2, 3, 4, 6, 12}
print(roznica_a_b)


#dodawanie elementu do zbioru
C = {1, 7, 4, 5}
C.add(2)
print(C)