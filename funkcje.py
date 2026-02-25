def hurra():
    print('Hurra!\n' * 50)

#hurra2 - nazwa funkcji
#n - parametr funkcji
#6 - argument funkcji
#hurra2(6) - wywolanie funkcji dla argumentu n = 6

def hurra2(n):
    print('Hurra!\n' * n)

hurra2(6)

#n = 10 tzw. parametr z argumentem domyslnym
def hurra3(n = 10):
    print('Hurra!\n' * n)

hurra3()

#jezeli funkcja poprostu wykonuje jakas czynnosc i nie mozemy wykorzystac dalej
#efektow jej pracy to jest to procedura

#pole calkowite graniastoslupa prawidlowego trojkatnego

def p_tr_rown(a):
    return a ** 2 * (3 ** 0.5) / 4

Pp = p_tr_rown(3 ** 0.25)

print(Pp)

def p_prst(a, b):
    return a * b

#psb = p_prst(5, 4)

def p_gran_praw_troj(a, b):
    return 2 * p_tr_rown(a) + 3 * p_prst(a, b)

pg = p_gran_praw_troj(7, 4)
print(pg)