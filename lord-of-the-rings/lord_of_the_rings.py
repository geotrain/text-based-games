import random

class Player:
    def __init__(self, name, race, class_type):
        self.name = name
        self.race = race
        self.class_type = class_type
        self.health = 100
        self.attack_power = 15
        self.level = 1
        self.experience = 0

class Creature:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

def explore_middle_earth(player):
    print(f"{player.name} is embarking on a journey through Middle-earth...")

    # Encounter a random creature
    creature = random.choice([Creature("Orc", 20, 8), Creature("Troll", 30, 12), Creature("Spider", 15, 10)])

    print(f"A wild {creature.name} appears!")

    while player.health > 0 and creature.health > 0:
        print(f"{player.name}'s health: {player.health}")
        print(f"{creature.name}'s health: {creature.health}")

        action = input("What will you do? (1. Attack, 2. Run) ")

        if action == "1":
            # Player attacks the creature
            damage = random.randint(1, player.attack_power)
            creature.health -= damage
            print(f"You deal {damage} damage to {creature.name}!")

            # Creature counter-attacks
            creature_damage = random.randint(1, creature.attack_power)
            player.health -= creature_damage
            print(f"{creature.name} counter-attacks and deals {creature_damage} damage to {player.name}!")
        elif action == "2":
            print(f"{player.name} runs away from the {creature.name}.")
            break
        else:
            print("Invalid choice. Try again.")

    if player.health <= 0:
        print(f"{player.name} was defeated. Game over.")
    elif creature.health <= 0:
        print(f"You defeated the {creature.name}! You gain experience.")
        player.experience += 10
        if player.experience >= 20:
            player.level += 1
            player.experience = 0
            print(f"Congratulations! {player.name} leveled up to level {player.level}!")

def main():
    player_name = input("Enter your character's name: ")
    player_race = input("Choose your race (Human, Elf, Dwarf): ")
    player_class = input("Choose your class (Warrior, Wizard, Ranger): ")
    player = Player(player_name, player_race, player_class)

    while player.health > 0:
        explore_middle_earth(player)

if __name__ == "__main__":
    main()

