def main():
    
    leg1 = float(input("Enter the length of the first leg: "))
    leg2 = float(input("Enter the length of the second leg: "))

    hypotenuse = (leg1 ** 2 + leg2 ** 2) ** 0.5

    print(f"The length of the hypotenuse is: {hypotenuse:.2f}")

if __name__ == "__main__":
    main()