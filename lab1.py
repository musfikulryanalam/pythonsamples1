Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 08:06:12) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #Author: Ryan Alam
>>> #Assignment Lab 1
>>> #Completed: 1/8/16
>>> 
>>> 
>>> #User will enter name, age, copany that he or she wishes to work for, and monthly salary
>>> name = input("Enter name")
Enter name Tyler Wood
>>> age = input("Enter age:)
	    
SyntaxError: EOL while scanning string literal
>>> age = input("Enter age:")
Enter age:20
>>> company = input(" Enter company you wish to work for:")
 Enter company you wish to work for:Google
>>> salary =input("Enter monthly salary you wish to earn in dollars")
Enter monthly salary you wish to earn in dollars 8000
>>> yearly = int(salary)
>>> print("My name is" , name , ", my agae is" , age)
My name is  Tyler Wood , my agae is 20
>>> print ("My namr is" , name , "my age is" , age)
My namr is  Tyler Wood my age is 20
>>> print ("My name is" , name , " , my age is")
My name is  Tyler Wood  , my age is
>>> (print "My namr is" , name , "," , "my age is" , age)
SyntaxError: invalid syntax
>>> print ("My name is" name , ", my age is" , age)
SyntaxError: invalid syntax
>>>  print ("My name is", name ,",", "my age is" , age)
 
SyntaxError: unexpected indent
>>> print ("My name is", name ,",", "my age is" , age)
My name is  Tyler Wood , my age is 20
>>> print ("I hope to work for", company, "and earn", yearly*12, "per year")
I hope to work for Google and earn 96000 per year
>>> 

>>> #second run through
>>> name = input("Enter name:")
Enter name:Ryan Alam
>>> age = input("Enter age:")
Enter age:22
>>> company = input("Enter company you wish to work for")
Enter company you wish to work for FaceBook
>>> salary = input("Enter monthly salary you wish to earn in dollars:")
Enter monthly salary you wish to earn in dollars:8500
>>> yearly = int(salary)
>>> print ("My name is" , name,", my age is" ,age,)
My name is Ryan Alam , my age is 22
>>> print(" I hope to work for" , company, " and earn" ,yearly*12, "per year")
 I hope to work for  FaceBook  and earn 102000 per year
>>> #User will enter name, age, copany that he or she wishes to work for, and monthly salary
