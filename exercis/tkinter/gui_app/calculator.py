import tkinter as tk 
app = tk.Tk()
app.title("Calculator")
app.geometry("300x400")
input = tk.Entry(app)
input.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

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
plush = tk.Button(app, text="+", width=2, height=2, command=lambda: get_value("+"))
minus = tk.Button(app, text="-", width=2, height=2, command=lambda: get_value("-"))
multiply = tk.Button(app, text="*", width=2, height=2, command=lambda: get_value("*"))
divide = tk.Button(app, text="/", width=2, height=2, command=lambda: get_value("/"))

equal = tk.Button(app, text="=", width=2, height=2, command=calculate)
clear = tk.Button(app, text="C", width=2, height=2, command=clear_value)

seven.grid(row=1, column=0)
eight.grid(row=1, column=1)
nine.grid(row=1, column=2)
divide.grid(row=1, column=3)
six.grid(row=2, column=0)
five.grid(row=2, column=1)
four.grid(row=2, column=2)
multiply.grid(row=2, column=3)
three.grid(row=3, column=0)
two.grid(row=3, column=1)
one.grid(row=3, column=2)
minus.grid(row=3, column=3)
zero.grid(row=4, column=0)
clear.grid(row=4, column=1)
equal.grid(row=4, column=2)
plush.grid(row=4, column=3)

app.mainloop()