print("======================Book Bazar====================")
print("1.mathematic(Rs:1000) (1.DBMS(RS:2000) (3.data science(Rs:3000) (4.cyber security(Rs:4000) (5.software egg(RS:5000))))")
mathematic_price = 0
DBMS_price = 0
data_science_price = 0
cybersecurity_price = 0
softwareegg_price = 0

option = int(input("enetr the choice"))

if option==1:
    book_name="mathematic"
    quantity=int(input("enter the quantity:"))
    mathematic_price=1000 * quantity
    
elif option==2:
    book_name="DBMS"
    quantity=int(input("enter the quantity:"))
    DBMS_price=2000 * quantity

elif option==3:
    book_name="data_science"
    quantity=int(input("enter the quantity:"))
    data_science_price=3000 * quantity

elif   option==4:
    book_name="cybersecurity"
    quantity=int(input("enter the quantity:"))
    cybersecurity_price=4000 * quantity

elif option==5:
    book_name="software egg"
    quantity=int(input("enter the quantity:"))
    softwareegg_price=5000 * quantity

else:
    print("Invailed choice")
print("Delivery option")
print("1.Home Delivery(Rs:1000) 2.pick up(free)")
Delivery_price=0
Delivery_option=int(input("enter your choice:"))
if Delivery_option==1:
    Delivery_price=1000
print("packing: 1.normal(500) 2.gift packking(500)")
packing_price=0
packing_option=int (input("enter the option"))
if packing_option==1:
    packing_price=500
elif packing_option==2:
    packking_price=1000 
print("Location: 1.KTM(5%) 2.Litipur(0%) 3.Bhaktpur(0%)")
tax_amount =0
Location_option =int(input("enetr your choice:"))
total = mathematic_price + DBMS_price + data_science_price + cybersecurity_price + softwareegg_price

if Location_option==1:
    tax_amount = total * 0.13
grand_total = total + Delivery_price + packing_price + tax_amount
print('product',book_name)
print('quatity',quantity)
print('delivery',Delivery_option)
print('tax',tax_amount)
print('grand',grand_total)







