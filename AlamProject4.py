#Ryan Alam
#Project 2
import random
import sys


#this function takes the number of days as range and creates a list using lower and upper bound for temperature. Returns and prints the list.
def initList(n,low,high):
    tempList=[]
    for i in range(n):
        tempList.append(random.uniform(low,high))
    tempList.sort()
    #print("Temperature List(sorted list):" ,tempList)
    return tempList

#this function is used to get the highest temperature from the list
def getHighest(tempList):
    largest = tempList[0]
    for i in range(1, len(tempList)):
        if tempList[i]> largest:
            largest = tempList[i]
    #print("Highest temperature:" , largest)
    return largest

#this function is used to get the lowest temperature from the list
def getLowest(tempList):
    smallest = tempList[0]
    for i in range(1, len(tempList)):
        if tempList[i] < smallest:
            smallest = tempList[i]
    #print("Lowest temperature(using calculation from getLowest() function):" , smallest)
    return smallest

#this function is used to calculate the average from the list
def getAverage(tempList):
    
    for i in range(1, len(tempList)):
        result = sum(tempList)/float(len(tempList))
    #print("Average temperature:" , result)
    return result
    
    

#main function where the above functions are called. Also this function prompts user to enter data, and used to compare data. 
def main():
    #user enters data needed, passes through the initList() function.
    days = input("How many days in this month:")
    n = int(days)
    print("Now you need to give a temperature range for this month")
    x = input("Enter lower bound of this month's temperature:")
    low = int(x)
    y = input("Enter upper bound of this month's temperature:")
    high = int(y)
    print()
    tempList = initList(n,low,high)
    print("Temperature List(sorted list):" , tempList)
    print()
    #following code calls the functions above 
    getHighest(tempList)
    print("Highest temperature(using calculation from getHighest() function):", getHighest(tempList))
    getLowest(tempList)
    print("Lowest temperature(using calculation from getLowest() function):" , getLowest(tempList))
    getAverage(tempList)
    print("Average temperature:" , getAverage(tempList))
    print()
    #following code used to compare max and min functions with calculations from the getHighest() and getLowest() functions.
    max(tempList)
    print("Highest temperature(from list using max function):" , max(tempList))
    min(tempList)
    print("Lowest temperature(from list using min function):" , min(tempList))
    #following code is used if max function is equal to getHighest() function.
    if max(tempList) == getHighest(tempList):
        print("I made it")
    else:
        print("I made a mistake")


#calls main() function
main()

#output
'''
Python 3.2.3 (default, Apr 11 2012, 07:12:16) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ================================ RESTART ================================
>>> 
How many days in this month:28
Now you need to give a temperature range for this month
Enter lower bound of this month's temperature:50
Enter upper bound of this month's temperature:70

Temperature List(sorted list): [50.79031406523741, 50.79431828935408, 51.237954890606346, 52.87398534733852, 52.91735495011882, 53.36834532255459, 53.5810511787058, 54.10231903303698, 55.19709245613674, 55.88718440165218, 56.20082701359899, 56.3637159361793, 56.73828649222809, 56.75266306405475, 57.6847811046352, 58.28455737896316, 58.652277667708496, 60.9009122440915, 62.50590331738076, 63.27136016078544, 63.40721200879266, 65.08666937410857, 65.73444750446367, 66.4445581498309, 68.23620041765761, 69.01094362872867, 69.36080113398641, 69.60797356984565]

Highest temperature(using calculation from getHighest() function): 69.60797356984565
Lowest temperature(using calculation from getLowest() function): 50.79031406523741
Average temperature: 59.10692893220648

Highest temperature(from list using max function): 69.60797356984565
Lowest temperature(from list using min function): 50.79031406523741
I made it
>>> ================================ RESTART ================================
>>> 
How many days in this month:31
Now you need to give a temperature range for this month
Enter lower bound of this month's temperature:70
Enter upper bound of this month's temperature:100

Temperature List(sorted list): [70.27456428689182, 72.87087639352164, 75.98723561268076, 76.23716699572947, 76.69030995779839, 76.79614253670653, 77.23244914094556, 77.52533947027781, 77.95923356836668, 78.1973728296456, 79.76118038277792, 81.02396957168466, 81.7289486271787, 82.22351260446246, 82.24290785408918, 83.44190430460723, 85.3631439000288, 85.64654153469858, 86.26828550192221, 87.32591256080616, 87.41300599441135, 88.99910939563227, 89.8414759585859, 89.85149977167478, 93.62973018803541, 95.46025414819212, 95.9566290887548, 96.89756847962272, 97.55598740049942, 98.4754461980192, 99.1457604659635]

Highest temperature(using calculation from getHighest() function): 99.1457604659635
Lowest temperature(using calculation from getLowest() function): 70.27456428689182
Average temperature: 84.77495047497457

Highest temperature(from list using max function): 99.1457604659635
Lowest temperature(from list using min function): 70.27456428689182
I made it
>>> 
,,,

