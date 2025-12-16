from random import randint
from time import sleep
wynik1 = 0
wynik2 = 0
wynik3 = 0
akcja = 0
while not ((wynik1 >= 5 or wynik2 >= 5 or wynik3 >= 5) and abs(wynik1 - wynik2 or wynik3 - wynik2 or wynik3 - wynik1) >= 2): #abs(x) = |x|
    akcja += 1  # akcja = akcja + 1
    print(f'akcja {akcja}')
    druzyna = randint(1, 3)
    if druzyna == 1:
        wynik1 += 1
    elif druzyna == 2:
        wynik2 += 1
    else:
        wynik3 += 1
    print(f'Wynik {wynik1} : {wynik2} : {wynik3}')
    sleep(0.25)
if wynik1 > wynik2 and wynik1 > wynik3:
    print('wygrala druzyna 1')
elif wynik2 > wynik1 and wynik2 > wynik3:
    print('wygrala druzyna 2')
elif wynik3 > wynik1 and wynik3 > wynik2:
    print('wygrala druzyna 3')