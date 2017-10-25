#Ryan Alam
#Lab 6
import math

#User will enter sides a and b to calculate side c and angle BAC
def main():
    print("Values to calculate side c and angle BAC")
    a = input("Enter side a:")
    sidea = float(a)
    b = input ("Enter side b:") 
    sideb = float(b)
    c = triangleside(sidea,sideb)
    print("side c:" , c)
    BAC = triangleangle(sidea,sideb)
    print("angle BAC:" ,BAC)

#function for side c
def triangleside(a,b):
    c = a*a + b*b
    c = math.sqrt(c)
    return c
#function for angle BAC
def triangleangle(a,b):
    BAC = a/b
  BAC  = math.degrees(math.atan(BAC))
    return BAC



#calls main functin
main()

#output
'''
Values to calculate side c and angle BAC
Enter side a:7.5
Enter side b:7.5
side c: 10.606601717798213
angle BAC: 45.0
>>> 
============== RESTART: C:/Users/ryan/Documents/cs299/lab 6.py ==============
Values to calculate side c and angle BAC
Enter side a:7.5
Enter side b:10
side c: 12.5
angle BAC: 36.86989764584402
>>> 
============== RESTART: C:/Users/ryan/Documents/cs299/lab 6.py ==============
Values to calculate side c and angle BAC
Enter side a:6
Enter side b:4.5
side c: 7.5
angle BAC: 53.13010235415598
,,,


