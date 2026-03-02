#zad 0.3
#a)
'''def suma_v(u, v):
    w = []
    for i in range(len(u)):
        suma = u[i] + v[i]
        w.append(suma)
    return w
u = [2, 7, 3]
v = [-1, 0, 4]
wynik = suma_v(u, v)
print(wynik)

def iloczyn_v(u, v):
    iloczyn2 = 0
    for i in range(len(u)):
        iloczyn = u[i] * v[i]
        iloczyn2 += iloczyn
    return iloczyn2

u = [2, 7, 3]
v = [-1, 0, 4]
wynik = iloczyn_v(u, v)
print(wynik)
'''
#zadanie 2.1
def czy_anagramy(s1, s2):
    '''if sorted(s1) == sorted(s2):
        return True
    else:
        return False'''
    return sorted(s1) == sorted(s2)
#print(czy_anagramy('nosek', 'keson'))
'''s1= 'nosek'
s2 = 'keson'
print(sorted(s1) == sorted(s2))
'''

#2.2
def jaki_trojkat(a, b, c):
    if a + b + c > 2 * max([a, b, c]) ** 2:
        if a ** 2 + b ** 2 + c ** 2 == 2 * max([a, b, c]) ** 2:
            print('prostokatny')
        elif a ** 2 + b ** 2 + c ** 2 > 2 * max([a, b, c]) ** 2:
            print('ostrokatny')
        elif a ** 2 + b ** 2 + c ** 2 < 2 * max([a, b, c]) ** 2:
            print('rozwartokatny')
    else:
        print('to niejest trojkat')
jaki_trojkat(10, 5, 12)