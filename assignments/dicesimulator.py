import random

def roll_dice():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    return dice1, dice2

def main():
    print("Welcome to the Dice Simulator!")
    while True:
        input("Press Enter to roll the dice...")
        dice1, dice2 = roll_dice()
        print(f"You rolled: {dice1} and {dice2}")
        
        if input("Do you want to roll again? (y/n): ").lower() != 'y':
            break
    print("Thanks for playing!")


if __name__ == '__main__':
    main()
