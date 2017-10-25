#Author: Ryan Alam
#Assignment: Lab #2
#Completed (or last revision): 1/9/17




#user will enter weight in pounds and height in inches
weight = input("Enter weight in pounds:")
weightnum= float(weight)
height = input("Enter height in inches:")
heightnum = float(height)

#calculation of BMI
bmi = (weightnum/(heightnum)**2*703)

#print out of results
print("You weight is:",weightnum)
print("You height is:" , heightnum)
print("Your BMI is: %.1f"  %bmi,)
print("Thank You!")

# output of results 
'''
Enter weight in pounds:102
Enter height in inches:56
You weight is: 102
You height is: 56.0
Your BMI is: 22.9
Thank You!
>>> 
>>> 
=============== RESTART: C:/Users/ryan/Documents/cs299/lab2.py ===============
Enter weight in pounds:160
Enter height in inches:71
You weight is: 160
You height is: 71.0
Your BMI is: 22.3
Thank You!
>>> 
=============== RESTART: C:/Users/ryan/Documents/cs299/lab2.py ===============
Enter weight in pounds:250
Enter height in inches:67
You weight is: 250
You height is: 67.0
Your BMI is: 39.2
Thank You!
>>> 
=============== RESTART: C:/Users/ryan/Documents/cs299/lab2.py ===============
Enter weight in pounds:200
Enter height in inches:70
You weight is: 200
You height is: 70.0
Your BMI is: 28.7
Thank You!
'''
