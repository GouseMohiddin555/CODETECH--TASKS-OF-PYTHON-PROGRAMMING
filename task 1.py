def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y

def main():
    print("Welcome to the basic calculator!")
    
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    while True:
        try:
            num2 = float(input("Enter the second number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
    
    print("\nSelect operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    while True:
        operation = input("Enter the operation (1/2/3/4): ")

        if operation == '1':
            result = add(num1, num2)
            print(f"The result of {num1} + {num2} is: {result}")
            break
        elif operation == '2':
            result = subtract(num1, num2)
            print(f"The result of {num1} - {num2} is: {result}")
            break
        elif operation == '3':
            result = multiply(num1, num2)
            print(f"The result of {num1} * {num2} is: {result}")
            break
        elif operation == '4':
            result = divide(num1, num2)
            print(f"The result of {num1} / {num2} is: {result}")
            break
        else:
            print("Invalid operation selected. Please choose a number between 1 and 4.")

if __name__ == "__main__":
    main()
