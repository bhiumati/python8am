#(Q1)
# users=[ 'ram','sita','gita']

# def show_users():
#     for name in users:
#         print(name)

# show_users()


# def add_users(name):
#     pass


# def remove_users(name):
#     pass

# users = ['ram', 'sita', 'gita']

# def show_users():
#     for name in users:
#         print(name)

# def add_user(name):
#     users.append(name)  

# def remove_user(name):
#     if name in users:
#         users.remove(name)  
#     else:
#         print(f"{name} not found in the list.")


# show_users()

# add_user('krishna')
# print("\nAfter adding Krishna:")
# show_users()

# remove_user('sita')
# print("\nAfter removing Sita:")
# show_users()



#(Q2)
# WAP to find largest number from list
# def find_largest(numbers):
#     pass

# def find_largest(numbers):
#     return max(numbers)
# numbers = [10, 20, 50, 5, 100, 35]
# largest = find_largest(numbers)
# print("The largest number is:", largest)



#(q3)

data =[1,2,3,4,5,6,7,8,9,10,2,4,7,8]
# remove duplicates from list

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 4, 7, 8]

# Remove duplicates by converting to a set, then back to a list
unique_data = list(set(data))

print("List after removing duplicates:", unique_data)

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 4, 7, 8]

unique_data = []
for num in data:
    if num not in unique_data:
        unique_data.append(num)

print("List after removing duplicates:", unique_data)








