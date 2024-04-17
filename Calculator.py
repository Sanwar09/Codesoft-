def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed"
    else:
        return x / y
print('''
            ---------Simple Calculator----------
            
            Please select any one opeartions:
            1.Addition(+)
            2.Substraction(-)
            3.Multiplication(*)
            4.Division(/)
            ''')
while True:
    try:
        choice = int(input("Enter operation choice (1/2/3/4): "))
        if choice in (1, 2, 3, 4):
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
    except ValueError:
        print("Invalid choice. Please enter a number between 1 and 4.")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if choice == 1:
    result = add(a, b)
    operation = "+"
    print("The Addition is:- ")
    print(f"{a} {operation} {b} = {result}")
elif choice == 2:
    result = subtract(a, b)
    operation = "-"
    print("The Substraction is:- ")
    print(f"{a} {operation} {b} = {result}")
elif choice == 3:
    result = multiply(a, b)
    operation = "*"
    print("The Multiplication is:- ")
    print(f"{a} {operation} {b} = {result}")
elif choice == 4:
    result = divide(a, b)
    operation = "/"
    print("The Division is:- ")
    print(f"{a} {operation} {b} = {result}")
