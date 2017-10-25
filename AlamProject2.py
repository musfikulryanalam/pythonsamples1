#Ryan Alam
#Project 2


import random
hidden = random.randint(1,100)
attempts = 0
guess = 0
print("Problem 1")
print("(This number is being printed for testing)", hidden)

while attempts < 3 and guess < 5:
    choice = input("Enter number between 1 and 100:")
    if not choice.isdigit():
        print("Input is not a numnber")
        attempts += 1
        guess +=1
    elif int(choice) < 1 or int(choice) > 100:
        print("Number out of range")
        attempts += 1
        guess +=1
    elif int(choice) < hidden:
        print("Guess is too small")
        attempts = 0
        guess +=1
    elif int(choice) > hidden:
        print("Guess is too big")
        attempts = 0
        guess +=1
    elif int(choice) == hidden:
        print("Good Job")
        correct = 1
        break;
    
if attempts == 3:
    print("Exceeded number of attempts due to wrong input(out of range or invalid entry)")
if attempts == 3 or guess == 5:
    print("You Lost")
    print("Correct Number is:" ,hidden)
else:
    print("Winner")
   


print()
print("Problem 2")

number = (input("Please enter any number: "))
numberinput = int(number)
perfect = 0
for i in range(1, numberinput):
    if(numberinput % i == 0):
        perfect = perfect + i
        print("factors:",i)
if (perfect == numberinput):
    print(numberinput, "is a perfect number")
else:
    print(numberinput, "is not a Perfect Number")
   
#Problem 1 outout
'''
Problem 1
(This number is being printed for testing) 22
Enter number between 1 and 100:l
Input is not a numnber
Enter number between 1 and 100:9999
Number out of range
Enter number between 1 and 100:0
Number out of range
Exceeded number of attempts due to wrong input(out of range or invalid entry)
You Lost
Correct Number is: 22
>>> 
============= RESTART: C:\Users\ryan\Documents\cs299\project2.py =============
Problem 1
(This number is being printed for testing) 94
Enter number between 1 and 100:93
Guess is too small
Enter number between 1 and 100:95
Guess is too big
Enter number between 1 and 100:50
Guess is too small
Enter number between 1 and 100:99
Guess is too big
Enter number between 1 and 100:6
Guess is too small
You Lost
Correct Number is: 94
>>> 
============= RESTART: C:\Users\ryan\Documents\cs299\project2.py =============
Problem 1
(This number is being printed for testing) 99
Enter number between 1 and 100:99
Good Job
Winner
>>> 
'''

#Problem 2 output
'''
============= RESTART: C:\Users\ryan\Documents\cs299\project2.py =============

Problem 2
Please enter any number: 6
factors: 1
factors: 2
factors: 3
6 is a perfect number
>>> 
============= RESTART: C:\Users\ryan\Documents\cs299\project2.py =============

Problem 2
Please enter any number: 28
factors: 1
factors: 2
factors: 4
factors: 7
factors: 14
28 is a perfect number
>>> 
============= RESTART: C:\Users\ryan\Documents\cs299\project2.py =============

Problem 2
Please enter any number: 325
factors: 1
factors: 5
factors: 13
factors: 25
factors: 65
325 is not a Perfect Number
>>> 
============= RESTART: C:\Users\ryan\Documents\cs299\project2.py =============

Problem 2
Please enter any number: 496
factors: 1
factors: 2
factors: 4
factors: 8
factors: 16
factors: 31
factors: 62
factors: 124
factors: 248
496 is a perfect number
>>> 
'''




