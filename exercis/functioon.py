# def add(x,y):
#     return x+y

# def total(a,b):
#     print(add(a,b))

# total(10,20)


# def take_mark():
#     pass
# # five subject marks return


# def total():
#     # calculate total marks
#     pass 

# def percentage():
#     # calculate percentage
#     pass

# def display():
#     # display result
#     pass

def add(x, y):
    return x + y

def total(a,b):
    print(add(a, b))

total(10, 20)
def take_marks():
    marks = []
    for i in range(1, 6):
        mark = float(input(f"Enter marks for subject {i}: "))
        marks.append(mark)
    return marks

def total_marks(marks):
    return sum(marks)

def percentage(marks):
    total = total_marks(marks)
    return (total / 500) * 100  
def display(marks):
    total_marks_result = total_marks(marks)
    percentage_result = percentage(marks)
    print(f"\nTotal Marks: {total_marks_result}/500")
    print(f"Percentage: {percentage_result:.2f}%")
    if percentage_result >= 40:
        print("Result: Pass")
    else:
        print("Result: Fail")
marks = take_marks()
display(marks)
































