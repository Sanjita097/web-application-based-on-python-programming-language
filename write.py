import os
import datetime

def add_data(Land):
    with open('file.txt','w')as file:
        for kitta_number, details in Land.items():
            Line=",".join([kitta_number,details["city"],details["direction"],int(details["area"]),int(details["price"]),details["status"]])
            file.write(Line+"\n")

def generate_invoice(invoice_type,customer_name,kitta_number,land_info,duration):
    total_amount=int(land_info["price"])*duration
    invoice_name=f"{customer_name}_{invoice_type}_invoice{datetime.datetime.today().strftime("%d-%m-%Y, %H-%M-%S")}.txt"
    with open('invoice.txt', 'w') as invoice:
            invoice.write(f"{invoice_type.capitalize()}Invoice")
            invoice.write(f"""
<--------------------------------------------------------------|
        Welcome to TechnoPropertyNepal.......                  |
<--------------------------------------------------------------|
  """)
           
            invoice.write(f"Customer Name:{customer_name}\n")
            invoice.write(f"Kitta Number : {kitta_number}\n")
            invoice.write(f"City/District: {land_info['city']}\n")
            invoice.write(f"Land Faced: {land_info['direction']}\n")
            invoice.write(f"Price:{land_info['price']}\n")
            invoice.write(f"Area: {land_info['area']} annas\n")
            invoice.write(f"Date and Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            invoice.write(f"Duration of Rent: {duration} month\n")
            invoice.write(f"\nTotal :{total_amount}")
            
            invoice.write(f"""
<--------------------------------------------------------------|
            Thank you for renting with us.......               |      
<--------------------------------------------------------------|
        """)
            
