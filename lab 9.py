#Ryan Alam
#Lab 9

#CashRegister class defined here
class CashRegister:
    def __init__(self):
        self._itemCount = 0
        self._totalPrice = 0.0

    def addItem(self, price):
        self._itemCount = self._itemCount + 1
        self._totalPrice = self._totalPrice + price

    def getTotal(self):
        return self._totalPrice

    def getCount(self):
        return self._itemCount

    def clear(self):
        self._itemCount = 0
        self._totalPrice = 0.0
    


#Calling the class
reg = CashRegister()


#Entering data. Exception handling used to validate data.

#Exception handling to check if data entered is integer. 
while True :
    countStr = input("Please enter number of items to be purchased:")
    try:
        itemCount = int(countStr)
        break
    except ValueError:
        print("You entered wrong data, please enter an integer as number of items to be purchased")
        pass

#Exception handling to check for non floats.
for i in range(itemCount) :
    while True :
        #print("Enter price for item %d" %(i+1))
        priceStr = input("Enter price for item #%d:" %(i+1))
        try :
            price = float(priceStr)
            print("Item %d price is $%0.2f" %(i+1, price))
            reg.addItem(price) 
            break
        except ValueError :
            print("You entered wrong data, please enter a real number as item price:")
            pass
   
#total of all items entered
print("Total number of items:", reg.getCount())
print("Your total cost is: $%.2f" %reg.getTotal())

#output
'''
>>> 
Please enter number of items to be purchased:3.5
You entered wrong data, please enter an integer as number of items to be purchased
Please enter number of items to be purchased:3
Enter price for item #1:13.a52
You entered wrong data, please enter a real number as item price:
Enter price for item #1:13.52
%Item 1 price is $13.52
Enter price for item #2:2.41
Item 2 price is $2.41
Enter price for item #3:21.90
Item 3 price is $21.90
Total number of items: 3
Your total cost is: $37.83
>>> ================================ RESTART ================================
>>> 
Please enter number of items to be purchased:5.6789
You entered wrong data, please enter an integer as number of items to be purchased
Please enter number of items to be purchased:5
Enter price for item #1:3
Item 1 price is $3.00
Enter price for item #2:2
Item 2 price is $2.00
Enter price for item #3:5
Item 3 price is $5.00
Enter price for item #4:6
Item 4 price is $6.00
Enter price for item #5:9
Item 5 price is $9.00
Total number of items: 5
Your total cost is: $25.00
>>> ================================ RESTART ================================
>>> 
Please enter number of items to be purchased:4.8
You entered wrong data, please enter an integer as number of items to be purchased
Please enter number of items to be purchased:4
Enter price for item #1:13
Item 1 price is $13.00
Enter price for item #2:12.bnbnbnbnb
You entered wrong data, please enter a real number as item price:
Enter price for item #2:12
Item 2 price is $12.00
Enter price for item #3:6.adft6
You entered wrong data, please enter a real number as item price:
Enter price for item #3:6
Item 3 price is $6.00
Enter price for item #4:4
Item 4 price is $4.00
Total number of items: 4
Your total cost is: $35.00
>>> 
'''



