#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from datetime import datetime

booking = []
data = []
checkedOut =[]


print ("**********************")
print ("Welcome to Tayor's Pets Hotel")

#front desk for the user
def userLogin():
    staff = False
    
    while staff == False:
        login = input("Enter your username: ")
        passw= int(input("Enter your password: "))
    
        if login == "a" and passw == 1:
            print ("********************************")
            print ("login successfull ^9_^9 ")
            print ("********************************")
            staff = True
        else:
            print ("Username or password incorrect")
        

    
userLogin()

#THE USER CHOOSE THE TYPE OF THE PET AND GET THE ROOM ACCORDING TO THE PET TYPE
def petFunction():
    print ("1. 60 rooms for dogs and cats \n2. 80 rooms for birds \n3. 100 rooms for rodent")
    print("\n Please choose the type of the pet \n 1. Dog   \n 2. cat \n 3. bird \n 4. Rodent")
    print("press 0 to exit")
    petTypeCheck = False
    while petTypeCheck == False:
        import random
        petType = input("Enter the pet type: ")
        if(petType == 0):
            break
        elif (petType == 'dog' or petType == 'cat'):
            hotelRoom =random.randint(1,61)
            print ("Your hotel room > " 'A'+str(hotelRoom))
            petTypeCheck = True
        elif (petType == 'bird'):
            hotelRoom = random.randint(61,141)
            print ("Your hotel room > " 'B'+str(hotelRoom))
            petTypeCheck = True 
        elif (petType == 'rodent'):
            hotelRoom = random.randint(142,242)
            print ("Your hotel Room > " 'C'+str(hotelRoom))
            petTypeCheck = True
        else:
            print("We dont have the type of the pet here")
            petType = input("Enter the pet type: ")
            petTypeCheck = False
            
    petName = input("enter your pet's name >>>> ")
    print ("your pet's name is " + petName)
    print ("********************************")
    
    petNameCheck = False
    while petNameCheck == False:
        petNameCon = int(input("\n enter 1 to continue \n enter 0 to exit "))
        if (petNameCon == 0):
            break
        if(petNameCon == 1):
            print ("OK, wait a moment")
            petNameCheck = True
        else:
            ("Please enter number that has been listed above ^^^")
            petNameCheck = False
            
            
            


#BOOKINGNUMBER
    
    
    booking_ID = int(datetime.now().strftime("%Y%m%d%H%M%S"))
    print ("Your Booking ID is " 'TPH',booking_ID)
    print ("********************************")
    

    dateCheckIn = datetime.now().strftime("%Y -%m -%d / %H:%M:%S")
    
    print ("********************************")
    print ("Date checked in = ")
    print (dateCheckIn)
    print ("********************************")
    
    booking.append ([petType, petName, hotelRoom, booking_ID, dateCheckIn])
    print(booking)

    programStart()
    
def searching():
    global booking
    searchDetail = input("Please enter the Booking ID > ")
    for element in booking:
        if searchDetail in element:
            print("It's listed here !")
            print(element)
            return True
      

    programStart()
            
        

    
def checkOut():
    global booking    
    checkOut = int(input("Please enter the Booking ID >"))
    for element in booking:
        for e in element:
            if checkOutFunc == e:
                checkedOut.append(element)
                booking.remove(element)
                print(checkedOut)
            
    petPayment = int(input("1.Dogs $50 per day \n2. Cats $50 per day \n3. Birds $30 per day \n4. Rodent $27 per day"))
    if (petPayment == 1 ):
        totalDays = int(input("How many days has your pet stayed? " ))
        payment = totalDays * 50
        print ("So your total payment will be $"+str(payment))
        print ("*********************")
        print ("*****RECEIPT*****")
        print ("Pet Type = Dog")
        print ("Total Days = ",totalDays )
        print ("Total Fees > $"+str(payment))
        print ("*****Thank You*****")
        print ("*********************")
        
    elif (petPayment == 2):
        totalDays = int(input("How many days has your pet stayed ? " ))
        payment = totalDays * 50
        print ("So your total payment will be $"+str(payment))
        print ("**********************")
        print ("*****RECEIPT*****")
        print("petType = Cat")
        print ("Total days = ",totalDays)
        print ("Total Fees > $"+str(payment))
        print ("*****Thankyou*****")
        print("***********************")
        
    elif (petPayment == 3):
        totalDays = int(input("How many days has your pet stayed ? " ))
        payment = totalDays * 30
        print ("So your total payment will be $"+str(payment))
        print ("**********************")
        print ("*****RECEIPT*****")
        print("petType = Birds")
        print ("Total days = ",totalDays)
        print ("Total Fees > $"+str(payment))
        print ("*****Thankyou*****")
        print("***********************")
    
    elif (petPayment == 4):
        totalDays = int(input("How many days has your pet stayed ? " ))
        payment = totalDays * 27
        print ("So your total payment will be $"+str(payment))
        print ("**********************")
        print ("*****RECEIPT*****")
        print("petType = Rodent")
        print ("Total days = ",totalDays)
        print ("Total Fees > $"+str(payment))
        print ("*****Thankyou*****")
        print("***********************")
        
    programStart()
        
    
    
        
def historyList():
    global checkedOut
    print ("Here is the history list who booked out")
    print ("The format of the history list \n[pet type, pet name, hotelRoom, Booking ID, date check in]")
    print (checkedOut)

        

def programStart():
    while(True):
        menuInput = int(input("Please choose the service \n1.Checkin \n2.Checkout \n3.search for details \n4.History List \n5. press 0 to exit "))
        if (menuInput == 1):
            petFunction()
        elif (menuInput == 2):
            checkOut()
        elif (menuInput == 3):
            searching()
        elif (menuInput == 4):
            historyList()
        elif (menuInput == 5):
            break
programStart()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




