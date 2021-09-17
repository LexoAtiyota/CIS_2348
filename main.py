print("Davy's auto shop services : \nOil change -- $35\nTire rotation -- $19\nCar wash -- $7\nCar wax -- $12")
shopService1=input("\nSelect first service: \n")#asking user to enter service 1
shopService2=input("Select second service: \n")# asking user to enter service 2
totalServiceAmount=0#variable to store service total amount
print("\nDavy's auto shop invoice Service\n")#print invoice
#checking first service
if(shopService1.lower()=="oil change"):#oil change service
    print("Service 1 : Oil change, $35") #print oil change details
totalServiceAmount=totalServiceAmount+35 #add oil change $35 to total

elif(shopService1.lower()=="tire rotation"): #tire rotation service
    print("Service 1 : Tire rotation, $19") #print Tire rotation, $19
    totalServiceAmount=totalServiceAmount+19 #add tire rotation $19 to total
elif(shopService1.lower()=="car wash"):#car wash
    print("Service 1 : Car Wash, $7") #print car wash $7
    totalServiceAmount=totalServiceAmount+7 #add car wash $7 to total
elif(shopService1.lower()=="car wax"):#car wax Service
    print("Service 1 : Car Wax, $12")#print car wax $12
    totalServiceAmount=totalServiceAmount+12 #add car wax $12 to total
elif(shopService1=="-"):#when no service
    print("Service : No service")
#check which service is selected as second service
if(shopService2.lower()=="oil change"):#when oil change service
    print("Service 2 Oil change, $35") #print oil change $35
totalServiceAmount=totalServiceAmount+35 #add oil change cost $35 to total
elif(shopService2.upper()=="tire rotation"):#tire rotation service
    print("Service 2 : Tire rotation, $19") #print Tire rotation, $19
    totalServiceAmount=totalServiceAmount+19 #add tire rotation $19 to total
elif(shopService2.lower()=="car wash"):#car wash
    print("Service 2 : Car Wash, $7") #print car wash $7
totalServiceAmount=totalServiceAmount+7 #add car wash $7 to total
elif(shopService2.lower()=="car wax"): #car wax Service
print("Service 2 : Car Wax, $12") #print car wax $12
totalServiceAmount=totalServiceAmount+12 #add car wax $12 to total
elif(shopService2=="-"):#no service
    print("Service 2: No service")
#display total Service cost
print("\nTotal : $",totalServiceAmount