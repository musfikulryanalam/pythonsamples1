




NMAX = 1
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


