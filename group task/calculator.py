def get_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_operation():
    operations = ['+', '-', '*', '/', '%', '**', '//']
    print("\nAvailable operations:")
    print(" +  (Addition)")
    print(" -  (Subtraction)")
    print(" *  (Multiplication)")
    print(" /  (Division)")
    print(" %  (Modulus)")
    print(" ** (Exponentiation)")
    print(" // (Floor Division)")
    while True:
        op = input("Choose an operation from above: ").strip()
        if op in operations:
            return op
        else:
            print("Invalid operation. Please select a valid one.")

def calculate(a: float, b: float, op: str) -> float:
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b
    elif op == '%':
        if b == 0:
            raise ZeroDivisionError("Cannot take modulus by zero.")
        return a % b
    elif op == '**':
        return a ** b
    elif op == '//':
        if b == 0:
            raise ZeroDivisionError("Cannot perform floor division by zero.")
        return a // b
    else:
        raise ValueError("Unknown operation.")

def main():
    print("Welcome to the Python Calculator\n")
    while True:
        try:
            a = get_number("Enter first number: ")
            b = get_number("Enter second number: ")
            op = get_operation()
            result = calculate(a, b, op)
            print(f"\nResult of {a} {op} {b} = {result}")
        except ZeroDivisionError as zde:
            print(f"Error: {zde}")
        except Exception as e:
            print(f"Something went wrong: {e}")
        cont = input("\nDo you want to perform another calculation? (y/n): ").strip().lower()
        if cont != 'y':
            print("Thank you for using the calculator. Goodbye!")
            break

if __name__ == "__main__":
    main()
