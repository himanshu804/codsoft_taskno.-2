def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Error: Cannot divide by zero"

def calculator():
    print("Welcome to the Simple Calculator!")
    print("Available operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    choice = input("Enter your operation choice (1/2/3/4): ")

    if choice == "1":
        result = add(num1, num2)
        operator = "+"
    elif choice == "2":
        result = subtract(num1, num2)
        operator = "-"
    elif choice == "3":
        result = multiply(num1, num2)
        operator = "*"
    elif choice == "4":
        result = divide(num1, num2)
        operator = "/"
    else:
        print("Invalid choice. Please try again.")
        return

    print(f"{num1} {operator} {num2} = {result}")

calculator()
