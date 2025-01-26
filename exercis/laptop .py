print("===============================laptop bazar===========================")
print("1.lenovo(Rs:50000) (2.Hp(Rs:80000) (3.apple(Rs150000) 4.accer(Rs:70000) 5.dell(Rs:90000))")
lenovo_price = 0
Hp_price = 0
accer_price=0
dell_price=0
apple_price =0
product_name=0
quantity =0

option = int (input("enter your choice:"))

if option==1:
    product_name = "lenovo"
    quantity=int(input("enetr the quantity:"))
    lenovo_price = 50000 * quantity

elif option==2:
    product_name = "Hp"
    quantity = int(input("enter the quantity:"))
    Hp_price = 80000 * quantity
    
elif option==3:
    product_name = "apple"
    quantity = int(input("eneter thw=e quantity:"))
    apple_price = 150000*quantity

elif option==4:
    product_name="accer" 
    quantity=int(input("enter the quantity:"))
    accer_price= 70000 * quantity

elif option==5:
    product_name="dell"
    quantity=int(input("enter the quantity:"))
    dell_price=90000 * quantity
       
else:
    print("Invalied choice")

print ("Delivery option") 
print("1.Home Delivery(Rs:2000) 2.Pick up(Free)")
Delivery_price = 0
Delivery_option = int(input("enter your choice:")) 
if Delivery_option ==1:
    Delivery_price = 2000
print("packing: 1.normal(Rs:1000) \n2. gift packing(Rs:5000)")
packing_price = 0
packing_option=int(input('enter the option'))
if  packing_option==1:
     packing_price=1000
elif packing_option==2:
     packing_price=5000

print("Location: 1.KTM(15%) 2.Litipur(0%) 3.Bhaktpur(5%)")
tax_amount =0
Location_option =int(input("enetr your choice:"))
total = lenovo_price + Hp_price + apple_price + accer_price + dell_price
if Location_option==1:
    tax_amount = total * 0.13
grand_total = total + Delivery_price + packing_price + tax_amount
print('product',product_name)
print('quatity',quantity)
print('delivery',Delivery_option)
print('tax',tax_amount)
print('grand',grand_total)