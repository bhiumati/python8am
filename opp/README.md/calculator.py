 Function to add two numbers:
def add(x, y):
    return x + y

: Function to subtract two numbers:
def subtract(x, y):
    return x - y

 Function to multiply two numbers:
def multiply(x, y):
    return x * y

 Function to divide two numbers:
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

 Function to display the menu:
def display_menu():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

 Main program loop:
def calculator():
    while True:
        display_menu()
        choice = input("Enter choice (1/2/3/4/5): ")

        if choice == '5':
            print("Exiting the calculator. Goodbye!")
            break
        
        Checking if the user input is valid:
        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Please enter numeric values.")
                continue

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")
        else:
            print("Invalid choice! Please select a valid operation.")
            strat the calculator:
            calculator()
