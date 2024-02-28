# app.py

def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiplication(x, y):
    return x * y


if __name__ == "__main__":
    print("Simple CLI Calculator")
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        exit(1)

    sum_result = add(num1, num2)
    difference_result = subtract(num1, num2)
    multiplication_result = multiplication(num1, num2)

    print(f"Addition Result: {num1} + {num2} = {sum_result}")
    print(f"Subtraction Result: {num1} - {num2} = {difference_result}")
    print(f"Multiplication Result: {num1} * {num2} = {multiplication_result}")
