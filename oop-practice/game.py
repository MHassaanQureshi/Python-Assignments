class Character:
    def __init__(self, name, power):
        self.name = name
        self.health = 100
        self.power = power

    def attack(self, opponent):
        if opponent.health > 0:
            if self.power == "fire":
                print(f"{self.name} uses Fire Attack!")
                opponent.health -= 20
            elif self.power == "water":
                print(f"{self.name} uses Water Attack!")
                opponent.health -= 10
        else:
            print(f"{opponent.name} is already dead!")
        
        opponent.health = max(opponent.health, 0)  # Prevent negative health

    def heal(self):
        print(f"{self.name} heals!")
        self.health += 20
        self.health = min(self.health, 100)  # Max health cap

    def status(self):
        return f"{self.name} | Health: {self.health} | Power: {self.power}"

player1 = Character("Player1", "fire")
player2 = Character("Player2", "water")

print("#" * 20)
print(player1.status())
print(player2.status())
print("#" * 20)

while player1.health > 0 and player2.health > 0:
    print("\n--- Player1's turn ---")
    action = input("Attack or Heal? ").lower()
    if action == "attack":
        player1.attack(player2)
    elif action == "heal":
        player1.heal()
    print(player1.status())
    print(player2.status())

    if player2.health <= 0:
        print("\n💀 Player2 is dead! Player1 wins!")
        break

    print("\n--- Player2's turn ---")
    action = input("Attack or Heal? ").lower()
    if action == "attack":
        player2.attack(player1)
    elif action == "heal":
        player2.heal()
    print(player1.status())
    print(player2.status())

    if player1.health <= 0:
        print("\n💀 Player1 is dead! Player2 wins!")
        break
