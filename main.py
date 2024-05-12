
import datetime
from operation import rent_land, return_land
import write
import read

while True:
    print(
"""
<===============================You are here
for.==================================>
==========================1 : PRESS 1 FOR
READ DATA======================================
==========================2 : PRESS 2 FOR
RENT LAND==================================
==========================2 : PRESS 3 FOR
RETURN LAND==================================
==========================3 : PRESS 3 TO EXIT FROM
SYSTEM============================/n
"""
)
    # print("Select Operation:")
    # print("1. Read land data.")
    # print("2.Rent land.")
    # print("3.Return land.")
    # print("4.Exit")         
    choice =input("Enter your choice(1-4):")
    while True:
        if choice =="1" or choice=="2" or choice=="3" or choice=="4":
            break
        else:
            print("Invalid Choice.Please select number upto 3 not more than that.")
            choice=input("Enter Your choice again : ")
    if choice == "1": 
        print(read.display())
    elif choice=="2": 
       Kitta_number=(input("Enter kitta number:"))
       Customer_name=input("Enter your name:")
       duration=int(input("How long do you want to rent this property? (In months) "))
       rent_land(Kitta_number,Customer_name,duration)
    elif choice=="3":
       kitta_number=input("Enter rented kitta number:")
       customer_name=input("Enter your name:")
       return_date=int(input("Enter returned date:"))
       return_land(kitta_number,customer_name,return_date)

    elif choice=="4":
         print("Program exit.")   
    else:
         print("Invalid choice")

    print("Do you want to perfome more operation:")
    print("1.yes")
    print("2.No")
    choice =input("Enter Your choice(1-2):")
    while True:
                if choice =="1":
                   continue_status=True
                   break
                elif choice =="2":
                    continue_status=False
                    break
                else:
                    print("Invalid Choicec")
                    choice=input("Enter Your choice again : ")
    
    if not continue_status:
                 break
    
  
