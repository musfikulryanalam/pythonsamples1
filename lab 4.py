#Ryan Alam
#LAB 4


     
count = 1

while count <= 3:
    choice = input('Please enter "english" or "metric:"')
    if choice == "metric" or choice == "english":
        weight= input("Enter weight between 100 and 200 pounds:")
        while not weight.isdigit() or int(weight) < 100 or int(weight) > 200 :
            weight= input("Enter weight between 100 and 200 pounds:")
            
      
        print("your weight is:",weight)
        break;
        

    else:
       count += 1

if count > 3:
    print("Reach max attempts")
    


      
    
    


