#rozwiązywanie równania kwadratowego

'''a = float(input('Podaj liczbe a =/= 0'))
b = float(input('Podaj liczbe b'))
c = float(input('Podaj liczbe c'))
delta = b ** 2 - 4 * a * c

if delta > 0:
    x1 = (-b - delta ** 0.5) / (2 * a)
    x2 = (-b + delta ** 0.5) / (2 * a)
    print(f'x1 = {x1} v x2 = {x2}')
elif delta == 0:
    x = (-b) / (2 * a)
    print('x1 = x2 = {}'.format(x))
else:
    print('brak rozwiązań')'''

#zadanie 12
'''pisemny_j_poski = int(input('pisemny polski'))
pisemny_j_obcy = int(input('pisemny obcy'))
pisemny_j_dodatkowy = int(input('pisemny dodatkowy'))
ustny_j_poski = int(input('ustny polski'))
ustny_j_obcy = int(input('ustny obcy'))'''

#zadanie 14
a = float(input('Podaj liczbe a =/= 0'))
b = float(input('Podaj liczbe b'))
c = float(input('Podaj liczbe c'))

if b == 0 and c == 0:
    print(f'wynik = 0')
if b == 0 and c !=0:
    if -c/a > 0:
        x1 = (-c/a) ** 0.5
        x2 = -((-c/a) ** 0.5)
        print(f'x1 = {x1} v x2 = {x2}')
    if -c/a <0:
        print('brak rozwiązań')
if c == 0 and b != 0:
    x1 = 0
    x2 = -(b)/(a)
    print(f'x1 = {x1} v x2 = {x2}')
if b != 0 and c != 0:  #else
    delta = b ** 2 - 4 * a * b
    if delta > 0:
        x1 = (-b - delta ** 0.5) / (2 * a)
        x2 = (-b + delta ** 0.5) / (2 * a)
        print(f'x1 = {x1} v x2 = {x2}')
    elif delta == 0:
        x = (-b) / (2 * a)
        print('x1 = x2 = {}'.format(x))
    else:
        print('brak rozwiązań')