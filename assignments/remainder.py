def main():
    value1 = int(input("Enter the first number: "))
    value2 = int(input("Enter the second number: "))
    divide = value1 / value2
    remainder = value1 % value2
    print(f"The remainder of {value1} divided by {value2} is: {remainder}")
    print(f"The result of {value1} divided by {value2} is: {divide}")

if __name__ == "__main__":
    main()