def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    return x / y

def modulus(x, y):
    return x % y

if __name__ == "__main__":
    while True:
        print("Select operation: + - * / %")
        op = input("Enter operator: ")

        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter valid numbers.")
            continue  # restart loop

        if op == '+':
            print("Result:", add(a, b))
        elif op == '-':
            print("Result:", subtract(a, b))
        elif op == '*':
            print("Result:", multiply(a, b))
        elif op == '/':
            print("Result:", divide(a, b))
        elif op == '%':
            print("Result:", modulus(a, b))
        else:
            print("Invalid operator.")

        again = input("Try again? (y/n): ").lower()
        if again != 'y':
            print("Goodbye!")
            break
