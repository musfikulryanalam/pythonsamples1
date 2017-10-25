#Ryan Alam
#Project 3

global pizzaSize
def getSize():
    count = 0
    while count < 3:
        pizzaSize = input('"Enter pizza size:"')
        if pizzaSize == "10":
            print("The size you have chosen is:" , pizzaSize,"inches")
            return 10.99
        elif pizzaSize == "12":
            print("The size you have chosen is:" , pizzaSize,"inches")
            return 12.99
        elif pizzaSize == "14":
            print("The size you have chosen is:" , pizzaSize, "inches")
            return 14.99
        elif pizzaSize == "16":
            print("The size you have chosen is:" , pizzaSize , "inches")
            return 16.99
        else:
            print("Enter only those options")
            count +=1
    if count >= 3:
         print("very sorry")
         return -1
         
           
        
def getCrust():
    crust = input("Enter crust:")
    if crust == "hand-tossed":
       print("The crust you have chosen is:" , crust)
       return 0
    if crust == "thin crust":
       print("The crust you have chosen is:" , crust)
       return 0
    if crust == "deep-dish with thin-crust":
       print("The crust you have chosen is:" , crust)
       return 1
    if crust == "deep-dish":
       print("The crust you have chosen is:" , crust)
       return 2
    else:
        crust = "hand-tossed"
        print("You have  entered the wrong crust or chose not to enter a crust. Default crust will be chosen:" , crust)
        return 0

def applyDiscount():
    discount = input("Enter discount code:").lower()
    if discount == "Holiday10".lower():
        print("Your discount code is:" ,discount)
        return 0.1
    if discount == "Winter20".lower():
        print("Your discount code is:",discount)
        return 0.2
    if discount == "VIPmax".lower():
        print("Your discount code is:",discount)
        return 0.25
    else:
        print("No coupon")
        return 0
def cost(size,extra,discount):
    cost = (size + extra)*discount
    cost = (size + extra) - cost
    tax = cost * 0.0825
    aftertax = cost + tax
    print("Your total cost is: $%.2f"  %aftertax)
    return aftertax
     
    
    

def main():
   print("Pizza size and cost  as follows:")
   print("Pizza Size(inches)" ,"%13s" %"Cost") 
   print('10"',"%30s" %"$10.99")
   print('12"',"%30s" %"$12.99")
   print('14"',"%30s" %"$14.99")
   print('16"',"%30s" %"$16.99")
   size = float(getSize())
   print()
   print("Pizza crust and extra charge as follows:")
   print("Pizza Crust" ,"%26s" %" Extra Cost") 
   print("hand-tossed","%21s" %"$0.00")
   print("thin crust","%22s" %"$0.00")
   print("deep-dish with thin crust","%7s" %"$1.00")
   print("deep-dish","%23s" %"$2.00")
   extra = float(getCrust())
   print()
   print("Discount as follows:")
   print("Coupon Code" ,"%24s" %"Discount")
   print("Holiday10","%25s" %"%10 off")
   print("Winter20","%26s" %"%20 off")
   print("VIPmax","%28s" %"%25 off")
   discount = float(applyDiscount())
   print()
   cost(size,extra,discount)
   

main()
    
#output

'''
### Test 1
Pizza size and cost  as follows:
Pizza Size(inches)          Cost
10"                         $10.99
12"                         $12.99
14"                         $14.99
16"                         $16.99
"Enter pizza size:"15
Enter only those options
"Enter pizza size:"17
Enter only those options
"Enter pizza size:"11
Enter only those options
very sorry

Pizza crust and extra charge as follows:
Pizza Crust                 Extra Cost
hand-tossed                 $0.00
thin crust                  $0.00
deep-dish with thin crust   $1.00
deep-dish                   $2.00
Enter crust:



### Test 2
Pizza size and cost  as follows:
Pizza Size(inches)          Cost
10"                         $10.99
12"                         $12.99
14"                         $14.99
16"                         $16.99
"Enter pizza size:"17
Enter only those options
"Enter pizza size:"16
The size you have chosen is: 16 inches

Pizza crust and extra charge as follows:
Pizza Crust                 Extra Cost
hand-tossed                 $0.00
thin crust                  $0.00
deep-dish with thin crust   $1.00
deep-dish                   $2.00
Enter crust:pan crust
You have  entered the wrong crust or chose not to enter a crust. Default crust will be chosen: hand-tossed

Discount as follows:
Coupon Code                 Discount
Holiday10                   %10 off
Winter20                    %20 off
VIPmax                      %25 off
Enter discount code:Winter20
Your discount code is: winter20

Your total cost is: $14.71



### Test 3
Pizza size and cost  as follows:
Pizza Size(inches)          Cost
10"                         $10.99
12"                         $12.99
14"                         $14.99
16"                         $16.99
"Enter pizza size:"12
The size you have chosen is: 12 inches

Pizza crust and extra charge as follows:
Pizza Crust                 Extra Cost
hand-tossed                 $0.00
thin crust                  $0.00
deep-dish with thin crust   $1.00
deep-dish                   $2.00
Enter crust:deep-dish
The crust you have chosen is: deep-dish

Discount as follows:
Coupon Code                 Discount
Holiday10                   %10 off
Winter20                    %20 off
VIPmax                      %25 off
Enter discount code:
No coupon

Your total cost is: $16.23



### Test 4
Pizza size and cost  as follows:
Pizza Size(inches)          Cost
10"                         $10.99
12"                         $12.99
14"                         $14.99
16"                         $16.99
"Enter pizza size:"14
The size you have chosen is: 14 inches

Pizza crust and extra charge as follows:
Pizza Crust                 Extra Cost
hand-tossed                 $0.00
thin crust                  $0.00
deep-dish with thin crust   $1.00
deep-dish                   $2.00
Enter crust:thin crust
The crust you have chosen is: thin crust

Discount as follows:
Coupon Code                 Discount
Holiday10                   %10 off
Winter20                    %20 off
VIPmax                      %25 off
Enter discount code:VIPmax
Your discount code is: vipmax

Your total cost is: $12.17



### Test 5(testing for case insentivity for coupon codes. Doing two test for this case. Using test case 4 example to see if correct charge still comes with random upper and lower case)
Pizza size and cost  as follows:
Pizza Size(inches)          Cost
10"                         $10.99
12"                         $12.99
14"                         $14.99
16"                         $16.99
"Enter pizza size:"10
The size you have chosen is: 10 inches

Pizza crust and extra charge as follows:
Pizza Crust                 Extra Cost
hand-tossed                 $0.00
thin crust                  $0.00
deep-dish with thin crust   $1.00
deep-dish                   $2.00
Enter crust:thin crust
The crust you have chosen is: thin crust

Discount as follows:
Coupon Code                 Discount
Holiday10                   %10 off
Winter20                    %20 off
VIPmax                      %25 off
Enter discount code:HoLiDaY10
Your discount code is: holiday10

Your total cost is: $10.71
>>> 
============ RESTART: C:\Users\ryan\Documents\cs299\project 3.py ============
Pizza size and cost  as follows:
Pizza Size(inches)          Cost
10"                         $10.99
12"                         $12.99
14"                         $14.99
16"                         $16.99
"Enter pizza size:"14
The size you have chosen is: 14 inches

Pizza crust and extra charge as follows:
Pizza Crust                 Extra Cost
hand-tossed                 $0.00
thin crust                  $0.00
deep-dish with thin crust   $1.00
deep-dish                   $2.00
Enter crust:thin crust
The crust you have chosen is: thin crust

Discount as follows:
Coupon Code                 Discount
Holiday10                   %10 off
Winter20                    %20 off
VIPmax                      %25 off
Enter discount code:vipMAX
Your discount code is: vipmax

Your total cost is: $12.17
>>> 


============ RESTART: C:\Users\ryan\Documents\cs299\project 3.py ============
### Test 6(testing what happens if I put strings instead of correct pizza size.)
Pizza size and cost  as follows:
Pizza Size(inches)          Cost
10"                         $10.99
12"                         $12.99
14"                         $14.99
16"                         $16.99
"Enter pizza size:"lol
Enter only those options
"Enter pizza size:"***
Enter only those options
"Enter pizza size:"$$$$
Enter only those options
very sorry

Pizza crust and extra charge as follows:
Pizza Crust                 Extra Cost
hand-tossed                 $0.00
thin crust                  $0.00
deep-dish with thin crust   $1.00
deep-dish                   $2.00
Enter crust:

'''






    
