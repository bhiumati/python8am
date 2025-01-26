
# category =[
#     {'cid':1,'name':'Electronics'},
#     {'cid':2,'name':'Clothing'},
#     {'cid':3,'name':'Grocery'},
# ]


# products=[
#     {'pid':1,'name':'Mobile','price':20000,'quantity':2,'cid':1},
#     {'pid':2,'name':'Laptop','price':50000,'quantity':1,'cid':1},
#     {'pid':3,'name':'T-shirt','price':500,'quantity':3,'cid':2},
#     {'pid':4,'name':'Jeans','price':1500,'quantity':2,'cid':2},
#     {'pid':5,'name':'Rice','price':50,'quantity':5,'cid':3},
#     {'pid':6,'name':'Dal','price':100,'quantity':2,'cid':3},
# ]

# name = input(f"Enter the category name: ")
# for cat in category:
#     if cat['name']==name:
#         for product in products:
#             if product['cid']==cat['cid']:
#                 total = product['price'] * product['quantity']
#                 print(f"Product Name: {product['name']} Price: {product['price']}  Quantity: {product['quantity']}  Total: {total}")




# users=[
#     {'username':'admin','password':'admin'},
#      {'username':'ram','password':'ram'},
# ]

# username = input("Enter your username: ")
# for data in users:
#     if data['username'] == username:
        
#         password = input("Enter your password: ")
#         if data['password'] == password:
#             print("Welcome to the system!")
#             name = input(f"Enter the category name: ")
#             for cat in category:
#                 if cat['name'] == name:
#                     for product in products:
#                         if product['cid'] == cat['cid']:
#                             total = product['price'] * product['quantity']
#                             print(f"Product Name: {product['name']} Price: {product['price']} Quantity: {product['quantity']} Total: {total}")
              
#         else:
#             print("Your password is incorrect")
#     else:
#         print("your username is incorrect")





# products=[
#     {'pid':1,'name':'Mobile','price':20000,'quantity':2,'cid':1},
#     {'pid':2,'name':'Laptop','price':50000,'quantity':1,'cid':1},
#     {'pid':3,'name':'T-shirt','price':500,'quantity':3,'cid':2},
#     {'pid':4,'name':'Jeans','price':1500,'quantity':2,'cid':2},
#     {'pid':5,'name':'Rice','price':50,'quantity':5,'cid':3},
#     {'pid':6,'name':'Dal','price':100,'quantity':2,'cid':3},
#]





faculty=[
    {'fid':1,'name':'Science'},
    {'fid':2,'name':'Management'},
    {'fid':3,'name':'Humanities'}
]


students =[
    {'sid':1,'name':'ram','fid':1},
    {'sid':2,'name':'sita','fid':2},
    {'sid':3,'name':'gita','fid':3},
    {'sid':4,'name':'gopal','fid':1},
    {'sid':5,'name':'hari','fid':2},
    {'sid':6,'name':'nabin','fid':3},
    {'sid':7,'name':'sabin','fid':1},
    {'sid':8,'name':'abinash','fid':2},
    {'sid':9,'name':'anil','fid':3},
    {'sid':10,'name':'santosh','fid':1}
]

faculty_name = input("Enter a faculty name: ")

for faculty_id in faculty:
    if faculty_id['name'] == faculty_name:
        for student in students:
             if student['fid'] == faculty_id['fid']:
                print(f"Name:{student['name']}")








