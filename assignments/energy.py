mass = float(input("Enter the mass of the object (in kg): "))  
c = 299792458

def main():
    def calculate(mass):
        energy = mass * c**2
        return energy
    
    print(f"Energy = {calculate(mass)} joules")

if __name__ == "__main__":
    main()
