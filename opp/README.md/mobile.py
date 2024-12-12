print("===============mobile bazar===========")
print("1.oppo(Rs:16000) 2.samgsung(Rs:20000) 3.vivo(Rs:12000)")
option = int (input("Enter your choice"))
oppo_price = 0
samgsung_price = 0
vivo_price = 0
product_name = ""
quantity = 0
if option == 1:
quantity = int (input("Enter the quantity:"))
oppo_price = 16000*quantity
product_name = "oppo"
elif option == 2:
quantity = int(input("Enter the quantity:"))
samgsung_price = 20000*quantity
product_name = "samgsung"
elif option ==3:
quantity = int (input("Enter the quantity:"))
vivo_price = 12000*quantity
product_name = "vivo"
else:
print("Invalid option")
name = input("Enter your name:")
address = input("Enter your address:")
phone = input("Enetr your phone:")
print("===========================Invoice============================")
print("Name":,Name)
print("Address":,Address)
print("Phone":,Phone)
print("Product":,Product_name)
print("Quantity":,Quantity)
print("Total:" oppo_price+samgsung_price+vivo_price)
print("Thank you for shopping with us")
print("===========================Invoice========================================")






