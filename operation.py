import write
import read
from os.path import isfile, join
import datetime

def rent_land(kitta_number, customer_name, duration):
    Land = read.load_inventory()
    if kitta_number not in Land:
        print("Invalid Kitta Number. Please enter correct kitta number")
        return

    land_info = Land[kitta_number]
    print(land_info)
    if land_info['status'] == "Not Available":
        print("The land you wanted to rent is already rented. ")
        return
    
    Land[kitta_number]['status'] = 'Not Available'
    write.add_data(Land)

    write.generate_invoice('Rent', customer_name, kitta_number, land_info, duration)
    print("Land has been successfully rented. Please check your Invoice for more details.")


def return_land(kitta_number, customer_name, return_date):
    Land = read.load_inventory()
    if kitta_number not in Land:
        print("Invalid kitta Number. Please enter valid kitta number to rent land.")
        return

    land_info = Land[kitta_number]
    if land_info['status'] == " Available":
        print("This land is not rented. So this land cannot be returned.")
        return
    Land[kitta_number]['status'] = ' Available'
    write.add_data(Land)
    # write.generate_invoice('Return', customer_name, kitta_number, land_info, return_date)
    # print("Land returned successfully.")
   


    rented_month=int(input("enter rented month:"))
    returned_month=int(input("enter returned month:"))
    customer_name=input("enter your name:")
    fine_amount=apply_fine(rented_month,returned_month)
    write.add_data(Land)
    write.generate_invoice('Return',customer_name,kitta_number,land_info,return_date)
   
    

    

def apply_fine(rented_month,returned_month):
    """Apply fine to a particular land"""
    fine_amount=0
    late_month=returned_month-rented_month
    if late_month>0:
        fine_amount=late_month*10000
        print(f"You have returned the land {late_month} months late. The fine amount is Rs. {fine_amount}")
    else:
        print("No fine to be paid. Land returned on time.")