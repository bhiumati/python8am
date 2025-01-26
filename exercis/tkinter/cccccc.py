import tkinter as tk
def on_button_click(text):
    current = entry.get()
    if text == "AC":
        entry.delete(0, tk.END)
    elif text == "=":
        try:
            result = str(eval(current))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    else:
        entry.insert(tk.END, text)

app = tk.Tk()
app.title("Calculator")
app.geometry("300x400")  

app.config(bg="#f0f0f0")

entry = tk.Entry(app, width=16, font=("Arial", 24), borderwidth=2, relief="solid", justify="right", bg="#eaeaea")
entry.grid(row=0, column=0, columnspan=4, padx=20, pady=6)

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), ("AC", 4, 1), ("=", 4, 2), ("+", 4, 3)
]
for (text, row, col) in buttons:
    button = tk.Button(app, text=text, font=("Arial", 24), width=5, height=2, bg="#f1f1f1", relief="solid", command=lambda t=text: on_button_click(t))
    button.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")

for row in range(5):
    app.grid_rowconfigure(row, weight=1)
for col in range(4):
    app.grid_columnconfigure(col, weight=1)

app.mainloop()
