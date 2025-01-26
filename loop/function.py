#  def users (name,phone,address):
 #     print("Enter your name")
#     print("Enter your phone")
#      print("Enter your addrss")
#      user("ram", 88888,"ktm")


# def total (num):
#     x=0
#     for y in num:
#         x+=y
#     print(x)
#  Total ([10,20,30,40])


# def student (subject1,suject2,subjecr3,subject4, subject5)
#     subject1 = int(input"enetr subject1:")
#     subject2 = int(input("enter subject2:"))
#     subject3 = int(input("enter subject3:"))
#     subject2 = int(input("enter subject4:"))
#     subject3 = int(input("enter subject5:"))  
# Total = subject1+subject2+su+subject4+subject5
# pre = total/5
# print("total",Total)
# print("percentage",per)

 

def calculate_marks():
    marks = []
for i in range(1,6):
    mark=float(input(f"Enter the subject marks{i}"))
    mark.append(marks)
    total = sum(mark)
    per = (total/500)*100
    if per>95:
        grade='A+'
    elif per>80:
        grade='B+'
    elif per>70:
        grade='B'
    elif per>60:
        grade='C+'
    elif per >50:
        grade='C'
    else:
        print('fail')
    print(f"total mark:{total}")
    print(f"percentage:{per}")
    print(f"grade: {grade}")
calculate_marks()    

 