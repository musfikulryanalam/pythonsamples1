from random import randint

for i in range(1):
    a1 = randint(1,47)
    a2 = randint(1,47)
    a3 = randint(1,47)
    a4 = randint(1,47)
    a5 = randint(1,47)
for i in range(1):
    b1 = randint(1,47)
    b2 = randint(1,47)
    b3 = randint(1,47)
    b4 = randint(1,47)
    b5 = randint(1,47)
for i in range(1):
    c1 = randint(1,47)
    c2 = randint(1,47)
    c3 = randint(1,47)
    c4 = randint(1,47)
    c5 = randint(1,47)
for i in range(1):
    d1 = randint(1,47)
    d2 = randint(1,47)
    d3 = randint(1,47)
    d4 = randint(1,47)
    d5 = randint(1,47)
for i in range(1):
    e1 = randint(1,47)
    e2 = randint(1,47)
    e3 = randint(1,47)
    e4 = randint(1,47)
    e5 = randint(1,47)
for i in range(1):
    f1 = randint(1,47)
    f2 = randint(1,47)
    f3 = randint(1,47)
    f4 = randint(1,47)
    f5 = randint(1,47)
for i in range(1):
    g1 = randint(1,47)
    g2 = randint(1,47)
    g3 = randint(1,47)
    g4 = randint(1,47)
    g5 = randint(1,47)
for i in range(1):
    h1 = randint(1,47)
    h2 = randint(1,47)
    h3 = randint(1,47)
    h4 = randint(1,47)
    h5 = randint(1,47)
for i in range(1):
    i1 = randint(1,27)
    i2 = randint(1,47)
    i3 = randint(1,47)
    i4 = randint(1,47)
    i5 = randint(1,47)
    i6 = randint(1,27)
    i7 = randint(1,27)
    i8 = randint(1,27)
    

    print("Draw #1:",a1,a2,a3,a4,a5,"%4s"%i1)
    print("Draw #2:",b1,b2,b3,b4,b5,"%4s"%i2)
    print("Draw #3:",c1,c2,c3,c4,c5,"%4s"%i3)
    print("Draw #4:",d1,d2,d3,d4,d5,"%4s"%i4)
    print("Draw #5:",e1,e2,e3,e4,e5,"%4s"%i5)
    print("Draw #6:",f1,f2,f3,f4,f5,"%4s"%i6)
    print("Draw #7:",g1,g2,g3,g4,g5,"%4s"%i7)
    print("Draw #8:",h1,h2,h3,h4,h5,"%4s"%i8)


NMAX = 3
XMAX = 10




for n in range(1, NMAX + 1):
    print("%10d" % n, end="")

print()
for n in range(1, NMAX + 1):
    print("%10s" % "x ", end="")

print("\n", " ", "-" *35)




for x in range(1, XMAX +1):

    for n in range (1, NMAX + 1):
        print("%10.0f" %x ** n, end="")

    print()



"""
Draw #1: 27 9 38 40 18   13
Draw #2: 19 9 13 11 11   34
Draw #3: 2 29 26 29 22   31
Draw #4: 23 10 40 34 34   32
Draw #5: 40 25 33 4 13   45
Draw #6: 24 29 11 21 44   24
Draw #7: 5 4 19 17 4   21
Draw #8: 43 42 15 8 15   24
         1         2         3
        x         x         x 
   -----------------------------------
         1         1         1
         2         4         8
         3         9        27
         4        16        64
         5        25       125
         6        36       216
         7        49       343
         8        64       512
         9        81       729
        10       100      1000

        """
