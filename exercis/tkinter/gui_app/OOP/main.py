# class Car:
#     price = 100000

#     def model(self):
#         print("this is a model")
#     def add(self,x,y):
#         print(x,y)
# a=Car()
# print(a.price)
# a.model()
# a.add(10,20)


#(1)
# class Calculator:
#     def add(self,x,y):
#         print(x+y)
#     def mul(self,x,y):
#         print(x*y)
#     def div(self,x,y):
#         print(x/y)
#     def sub(self,x,y):
#         print(x-y)

# cal=Calculator()
# cal.add(10,20)
# cal.mul(4,10)
# cal.div(20,10)
# cal.sub(20,10)

# #(2)
# class Num:
#     n=5
#     for i in range(1,11,):
#          print(f'{n}*{i}={n*i}')
# m=Num()


#(3)
# class Student():
#     E=int(input("Enter the English marks:"))
#     N=int(input("Enter the Nepali marks:"))
#     M=int(input("Enter the Math marks:"))
#     C=int(input("Enter the Computer marks:"))
#     S=int(input("Enter the Science marks:"))
#     total=E+N+M+C+S
#     per=total/500*100
    
#     grade=0
#     if per>=90:





# class Calculator:
#     def add(self,x,y):
#         print(x+y)
#     def sub(self,x,y):
#         print(x-y)
#     def mul(self,x,y):
#         print(x*y)
#     def div(self,x,y):
#         print(x/y)

# cal=Calculator()
# cal.add(20,20)
# cal.sub(40,20)
# cal.mul(10,10)
# cal.div(20,5)




class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Point({self.x}, {self.y})"









