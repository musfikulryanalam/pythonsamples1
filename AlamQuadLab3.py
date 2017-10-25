#Ryan Alam
#Lab 3

from math import sqrt
x = sqrt(5)

#User going to input values for a,b,c of quadratic equation
a = input("Input value for a:")
aa = float(a)
b = input("Input value for b:")
bb = float(b)
c = input("Input value for c:")
cc= float(c)

#Quadratic equation
X = aa*x**2+bb*x+cc

#Conditions
if aa == 0.00:
    print("Not a quadratic equation")
elif X == 0.00:
    print("No real roots")
else:
    print("a coefficent is:", aa)
    print("b coefficent is:", bb)
    print("c coefficent is:", cc)
    print("Soulution is: %.2f" %X)





        
        
    

