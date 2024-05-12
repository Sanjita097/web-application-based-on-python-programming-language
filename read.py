
# def load_inventory():
#     Land=[]
#     with open('file.txt','r')as file: 
#         for line in file:
#             kitta_number, city, direction,area,price,status=line.strip().split(",")
#             Land[kitta_number]={
#                 "City":city,
#                 "Direction":direction,
#                 "Area":int(area),
#                 "Price":int(price),
#                 "Status":status
#             }
#     return Land   
#     # with open('file.txt','r')as file: 
#     #     alldata = file.read()
#     # return alldata
    

# load_inventory()

# def load_inventory():
#     Land = {}
#     with open('file.txt', 'r') as file: 
#         for line in file:
#             kitta_number, city, direction, area, price, status = line.strip().split(",")
#             Land[kitta_number] = {
#                 "city": city,
#                 "direction": direction,
#                 "area": int(area),
#                 "price": int(price),
#                 "status": status
               
            
#             }
#     return Land



# inventory = load_inventory()
# print(inventory)

def load_inventory():
    Land = {}
    with open("file.txt", "r") as file:
        for line in file:
            kitta_number, city, direction, area, price, status = line.strip().split(",")
            Land[kitta_number] = {
                "city": city,
                "direction": direction,
                "area": int(area),
                "price": int(price),
                "status": status,
            }

    return Land


def display(Land):
    print(
        "{:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(
            "Kitta No", "City", "Direction", "Area", "Price", "Status"
        )
    )
    for kitta_number, land_details in Land.items():
        print(
            "{:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(
                kitta_number,
                land_details["city"],
                land_details["direction"],
                land_details["area"],
                land_details["price"],
                land_details["status"],
            )
        )