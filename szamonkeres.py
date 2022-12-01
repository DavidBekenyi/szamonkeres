#1
"""
vez = input("vezetekneved? ")
ker = input("keresztneved? ")

print(vez, ker)
print(ker, vez)
"""
#2
"""
szam = int(input("szamot "))

print( szam-1, szam, szam+1)
"""
#3
"""
szam1 = int(input("szamot "))
szam2 = int(input("szamot "))

if szam2 > szam1:
    kisebb = szam1
    nagyobb = szam2
else:
    nagyobb = szam1
    kisebb= szam2

osszeg = nagyobb + kisebb
kulonbseg = nagyobb - kisebb
szorzat = nagyobb * kisebb
oszt = nagyobb / kisebb

print("osszeg:", osszeg, "kulonbseg:", kulonbseg, "szorzat:", szorzat, "hanyados", oszt)
"""
#4
"""
a = int(input("szamot "))
b = int(input("szamot "))
c = 2*a + 3*b
d = c - 2*a - 3*b

print(c, d)
"""
# 8 a 
"""
import random

list = []

for x in range(20):
    n = random.randint(1,12)
    list.append(n)

    if n % 2 != 0:
        print(n)
"""
# 8 b

"""
import random

list = []

for x in range(20):
    n = random.randint(1,12)
    list.append(n)

    if n % 2 == 0:
        print(n)
"""

list = []

ism = input("hanyszor ")
x = 0
while x != ism:
    x += 1
    input("szamot")
    list.append

print(list)   #gatya(nemjo)