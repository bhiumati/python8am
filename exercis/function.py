# def total(numbers):
#     x=0
#     for  a in numbers:
#         x += a
#     print(x)
# total([1,2,3,4,5,6,7,8,9,10])






# def mul():
#      for i in range(1,11):
#       print(f"3*{i}={3*i}")
#       mul(3)






def add():
    subject=int(input("enetr the nepali marks:"))
    subject=int(input("enetr the english marks:"))
    subject=int(input("enetr the math marks:"))
    subject=int(input("enetr the science marks:"))
    subject=int(input("enetr the computer marks:"))
    return[subject]
def total():
    x=0
    for i in add():
        x+=i 
        print(x)
def total_marks():
    per=(total()/500) * 100
    print(per)
total_marks ()





