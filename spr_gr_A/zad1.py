plik = open('prostokaty.txt')
dane = plik.readlines()
prostokaty = []
for x in dane:
    para = x.split()
    prostokat = (int(para[0]), int(para[1]))
    prostokaty.append(prostokat)
#1.1
prostokaty.sort(key = lambda x: x[0] * x[1])
p_min = prostokaty[0]
p_max = prostokaty[-1]
print(p_min[0] * p_min[1], p_max[0] * p_max[1])
#1.2
obwody = []
for p in prostokaty:
    obwod = 2*p[0] + 2*p[1]
    obwody.append(obwod)
rozne = set(obwody)
print(len(rozne))