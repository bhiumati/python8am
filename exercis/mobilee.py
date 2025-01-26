# print("===============================mobile bazar===========================")
# print("1.mi(Rs:20000) (2.Samsung(Rs:30000) (3.Iphone(Rs50000))")
# mi_price = 0
# Samsung_price = 0
# iphone_price =0
# product_name=0
# quantity =0

# option = int (input("enter your choice:"))

# if option==1:
#     product_name = "mi"
#     quantity=int(input("enetr the quantity:"))
#     mi_price = 20000 * quantity

# elif option==2:
#     product_name = "samsung"
#     quantity = int(input("enter the quantity:"))
#     Samsung_price = 30000 * quantity
 
# elif option==3:
#     product_name = "Iphone"
#     quantity = int(input("eneter thw=e quantity:"))
#     iphone_price = 50000*quantity
     
# else:
#     print("Invalied choice")

# print ("Delivery option") 
# print("1.Home Delivery(Rs:1000) 2.Pick up(Free)")
# Delivery_price = 0
# Delivery_option = int(input("enter your choice:")) 
# if Delivery_option ==1:
#     Delivery_price = 1000
# print("packing: 1.normal(Rs:1000) 2. gift packing(Rs:5000)")
# packing_price = 0
# packing_option=int(input('enter the option'))
# if  packing_option==1:
#      packing_price=1000
# elif packing_option==2:
#      packing_price=5000

# print("Location: 1.KTM(13%) 2.Litipur(0%) 3.Bhaktpur(0%)")
# tax_amount =0
# Location_option =int(input("enetr your choice:"))
# total = mi_price + Samsung_price + iphone_price
# if Location_option==1:
#     tax_amount = total * 0.13
# grand_total = total + Delivery_price + packing_price + tax_amount
# print('product',product_name)
# print('quatity',quantity)
# print('delivery',Delivery_option)
# print('tax',tax_amount)
# print('grand',grand_total)






# # age <18 and <40
# # 18-25 -> momo
# #24-35 -> beer
# # 35-45 -> pizza

# # age = int(input("enter the age:"))
# # if age>18:
# #     if age<25:
# #         print("congrtus u got only one momo")
# # elif age>25:
# #     if age<35:
# #         print("congruts u got a beer")




# #(2)
# print("==================Mobile Bazar==============")
# print("1. Mi(Rs:20000) 2. Samsung(Rs:30000) 3. Iphone(Rs:50000)")

# mi_price =0
# samsung_price =0
# iphone_price =0
# product_name=""
# quantity = 0
# option = int(input("Enter your choice: "))
# if option==1:
#     product_name = "Mi"
#     quantity = int(input("Enter the quantity: "))
#     mi_price = 20000 * quantity

# elif option==2:
#     product_name = "Samsung"
#     quantity = int(input("Enter the quantity: "))
#     samsung_price = 30000 * quantity

# elif option==3:
#     product_name = "Iphone"
#     quantity = int(input("Enter the quantity: "))
#     iphone_price = 50000 * quantity
# else:
#     print("Invalid choice")

# print("Delivey Option")
# print("1. Home Delivery(Rs:1000) 2. Pick up(Free)")
# delivery_price =0
# delivery_option = int(input("Enter your choice: "))
# if delivery_option==1:
#     delivery_price = 1000


# print("Packing: 1. Normal(Rs:1000) 2. Gift Packing(Rs:5000)")
# packing_price =0
# packing_option = int(input("Enter your choice: "))
# if packing_option==1:
#     packing_price = 1000
# elif packing_option==2:
#     packing_price = 5000

# print("Location: 1.KTM(13%) 2. Lalitpur(0%) 3. Bhaktapur(0%)")
# tax_amount =0
# location_option = int(input("Enter your choice: "))
# total = mi_price + samsung_price + iphone_price
# if location_option==1:
#     tax_amount = total * 0.13

# grand_total = total + delivery_price + packing_price + tax_amount
# print("======== Invoice =========")
# print(f"Product Name: {product_name}")
# print(f"Quantity: {quantity}")
# print(f"Total: {total}")
# print(f"Delivery Price: {delivery_price}")
# print(f"Packing Price: {packing_price}")
# print(f"Tax Amount: {tax_amount}")
# print(f"Grand Total: {grand_total}")





#(3)
# WAP to find largest number from list
# def find_largest(numbers):
#     pass
handle=open("record/user.txt","w")
handle.write("==========register=========\n")
print("==========register=========")
uname=input("Enter username:")
upassword=input("Enter password:")
handle.write(f"username:{uname},password:{upassword}\n")
handle.write("==========login=========\n")
print("==========login=========")
username=input("Enter username:")
password=input("Enter password:")
if username==uname:
    if password==upassword:
        print("sucess login")
        handle.write("sucess login")
        handle=open("record/book.txt","w")
        handle.write("ramayan\n")
        handle.write("munamadan\n")
        handle.write("sostik\n")
        print("======book_list=====")
        print("ramayan")
        print("munamadan")
        print("sostik")

    else:
        print("wromg password")
        handle.write("wromg password")
else:
    print("wrong username")
    handle.write("wrong username")

