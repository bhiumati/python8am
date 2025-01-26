#(1)>>
# import tkinter as tk
# app =tk.Tk()
# app = tk.Tk()
# app.title("GUI App")
# app.geometry("500x400")
# fn = tk.Label(app, text="Enter first number")
# fn.pack()
# n1 = tk.Entry(app)
# n1.pack()
# sn = tk.Label(app, text="Enter second number")
# sn.pack()
# n2 = tk.Entry(app)
# n2.pack()
# result = tk.Label(app, text="Result")
# result.pack()
# def add():
#     first_number = int(n1.get())
#     second_number = int(n2.get())
#     total = first_number + second_number
#     result.config(text="Result: " + str(total))
#     n1.delete(0, tk.END)
#     n2.delete(0, tk.END)

# button = tk.Button(app, text="Add Number", command=add)
# button.pack()
# app.mainloop()
# app.title("GUI App")
# app.geometry("500x400")
# fn = tk.Label(app, text="Enter first number")
# fn.pack()
# n1 = tk.Entry(app)
# n1.pack()
# sn = tk.Label(app, text="Enter second number")
# sn.pack()
# n2 = tk.Entry(app)
# n2.pack()
# result = tk.Label(app, text="Result")
# result.pack()
# def add():
#     first_number = int(n1.get())
#     second_number = int(n2.get())
#     total = first_number + second_number
#     result.config(text="Result: " + str(total))
#     n1.delete(0, tk.END)
#     n2.delete(0, tk.END)

# button = tk.Button(app, text="Add Number", command=add)
# button.pack()
# app.mainloop()


# #(2)>>

import tkinter as tk 
app = tk.Tk()
app.title("calculator")
app.geometry("500x600")
input=tk.Entry(app)
input.grid(row=0, column=0, columnspan=10,pady=10)

def get_value(value):
    a = input.get()
    input.delete(0, tk.END)
    input.insert(0, a + str(value))

def calculate():
    a = input.get()
    input.delete(0, tk.END)
    input.insert(0, eval(a))

def clear_value():
    input.delete(0, tk.END)

one  = tk.Button(app, text="1", width=2, height=2, command=lambda: get_value(1))
two = tk.Button(app, text="2", width=2, height=2, command=lambda: get_value(2))
three = tk.Button(app, text="3", width=2, height=2, command=lambda: get_value(3))
four = tk.Button(app, text="4", width=2, height=2, command=lambda: get_value(4))
five = tk.Button(app, text="5", width=2, height=2, command=lambda: get_value(5))
six = tk.Button(app, text="6", width=2, height=2, command=lambda: get_value(6))
seven = tk.Button(app, text="7", width=2, height=2, command=lambda: get_value(7))
eight = tk.Button(app, text="8", width=2, height=2, command=lambda: get_value(8))
nine = tk.Button(app, text="9", width=2, height=2, command=lambda: get_value(9))
zero = tk.Button(app, text="0", width=2, height=2, command=lambda: get_value(0))
equal = tk.Button(app, text="=", width=2, height=2, command=calculate)
minus = tk.Button(app, text="-", width=2, height=2, command=lambda: get_value("-"))
multiply = tk.Button(app, text="*", width=2, height=2, command=lambda: get_value("*"))
plush = tk.Button(app, text="+", width=2, height=2, command=lambda: get_value("+"))
divide = tk.Button(app, text="/", width=2, height=2, command=lambda: get_value("/"))
clear = tk.Button(app, text="AC", width=2, height=2, command=clear_value)

one.grid(row=1, column=0)
two.grid(row=1, column=1)
three.grid(row=1, column=2)
divide.grid(row=1, column=3)
four.grid(row=2, column=0)
five.grid(row=2, column=1)
six.grid(row=2, column=2)
multiply.grid(row=2, column=3)
seven.grid(row=3, column=0)
eight.grid(row=3, column=1)
nine.grid(row=3, column=2)
minus.grid(row=3, column=3)
zero.grid(row=4, column=0)
clear.grid(row=4, column=1)
equal.grid(row=4, column=3)
plush.grid(row=4, column=2)

app.mainloop()


# (3)
# import tkinter as tk
# import math

# app = tk.Tk()
# app.title("Scientific Calculator")
# app.geometry("600x700")

# input = tk.Entry(app)
# input.grid(row=0, column=0, columnspan=6, pady=10)

# def get_value(value):
#     current = input.get()
#     input.delete(0, tk.END)
#     input.insert(0, current + str(value))

# def calculate():
#     try:
#         result = eval(input.get())
#         input.delete(0, tk.END)
#         input.insert(0, result)
#     except Exception as e:
#         input.delete(0, tk.END)
#         input.insert(0, "Error")

# def clear_value():
#     input.delete(0, tk.END)

# def scientific_operations(op):
#     try:
#         value = float(input.get())
#         if op == 'sqrt':
#             input.delete(0, tk.END)
#             input.insert(0, math.sqrt(value))
#         elif op == 'sin':
#             input.delete(0, tk.END)
#             input.insert(0, math.sin(math.radians(value)))
#         elif op == 'cos':
#             input.delete(0, tk.END)
#             input.insert(0, math.cos(math.radians(value)))
#         elif op == 'tan':
#             input.delete(0, tk.END)
#             input.insert(0, math.tan(math.radians(value)))
#         elif op == 'log':
#             input.delete(0, tk.END)
#             input.insert(0, math.log(value))
#         # elif op == 'exp':
#         #     input.delete(0, tk.END)
#         #     input.insert(0, math.exp(value))
#     except Exception as e:
#         input.delete(0, tk.END)
#         input.insert(0, "Error")

# # Define buttons for the calculator
# buttons = [
#     ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('sqrt', 1, 4), ('log', 1, 5),
#     ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('sin', 2, 4), ('cos', 2, 5),
#     ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), ('tan', 3, 4), ('Ac', 3, 5),
#     ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('(', 4, 3), (')', 4, 4), ('=', 4, 5),

# ]

# # Create buttons for digits and operations
# for (text, row, col, *span) in buttons:
#     span = span or [1]  # Default to columnspan=1 if no span value provided
#     if text == 'AC':
#         btn = tk.Button(app, text=text, width=5, height=2, command=clear_value)
#     elif text == '=':
#         btn = tk.Button(app, text=text, width=5, height=2, command=calculate)
#     elif text in ('sqrt', 'sin', 'cos', 'tan', 'log', 'exp'):
#         btn = tk.Button(app, text=text, width=5, height=2, command=lambda op=text: scientific_operations(op))
#     else:
#         btn = tk.Button(app, text=text, width=5, height=2, command=lambda val=text: get_value(val))
#     btn.grid(row=row, column=col, columnspan=span[0])

# app.mainlo




