from random import randint
from time import sleep
wynik1 = 0
wynik2 = 0
akcja = 0
while not ((wynik1 >= 21 or wynik2 >= 21) and abs(wynik1 - wynik2) >= 2): #abs(x) = |x|
    akcja += 1  # akcja = akcja + 1
    print(f'akcja {akcja}')
    druzyna = randint(1, 2)
    if druzyna == 1:
        wynik1 += 1
    elif druzyna == 2:
        wynik2 += 1
    print(f'Wynik {wynik1} : {wynik2}')
    sleep(0.5)
if wynik1 > wynik2:
    print('wygrala druzyna 1')
else:
    print('wygrala druzyna 2')