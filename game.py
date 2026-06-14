import random
import json
import os

SAVE_FILE = "savegame.json"


class Player:
    def __init__(self, name, role):
        self.name = name
        self.role = role

        if role == "Warrior":
            self.health = 120
            self.attack = 15
            self.gold = 20

        elif role == "Mage":
            self.health = 80
            self.attack = 25
            self.gold = 30

        else:  # Rogue
            self.health = 100
            self.attack = 18
            self.gold = 50

        self.inventory = []
        self.achievements = []

    def show_stats(self):
        print("\n" + "=" * 40)
        print(f"Name: {self.name}")
        print(f"Class: {self.role}")
        print(f"Health: {self.health}")
        print(f"Attack: {self.attack}")
        print(f"Gold: {self.gold}")
        print("Inventory:", self.inventory)
        print("=" * 40)


def save_game(player, current_location):
    data = {
        "name": player.name,
        "role": player.role,
        "health": player.health,
        "attack": player.attack,
        "gold": player.gold,
        "inventory": player.inventory,
        "achievements": player.achievements,
        "location": current_location
    }

    with open(SAVE_FILE, "w") as f:
        json.dump(data, f)

    print("Game saved successfully.")


def load_game():
    if not os.path.exists(SAVE_FILE):
        return None, None

    with open(SAVE_FILE, "r") as f:
        data = json.load(f)

    player = Player(data["name"], data["role"])

    player.health = data["health"]
    player.attack = data["attack"]
    player.gold = data["gold"]
    player.inventory = data["inventory"]
    player.achievements = data["achievements"]

    return player, data["location"]


def achievement(player, text):
    if text not in player.achievements:
        player.achievements.append(text)
        print(f"\n🏆 Achievement Unlocked: {text}\n")


def battle(player, enemy_name, enemy_health, enemy_attack):
    print(f"\n⚔ A {enemy_name} appears!")

    while enemy_health > 0 and player.health > 0:

        print(f"\nYour HP: {player.health}")
        print(f"{enemy_name} HP: {enemy_health}")

        action = input("Attack or Run? ").lower()

        if action == "run":
            chance = random.randint(1, 100)

            if chance <= 50:
                print("You escaped!")
                return True

            print("Escape failed!")

        damage = random.randint(
            player.attack - 3,
            player.attack + 3
        )

        enemy_health -= damage

        print(f"You deal {damage} damage!")

        if enemy_health <= 0:
            print(f"You defeated the {enemy_name}!")
            reward = random.randint(10, 30)
            player.gold += reward
            print(f"You found {reward} gold.")
            return True

        enemy_damage = random.randint(
            enemy_attack - 2,
            enemy_attack + 2
        )

        player.health -= enemy_damage

        print(f"The {enemy_name} hits you for {enemy_damage}.")

    if player.health <= 0:
        print("\n☠ You have fallen.")
        return False

    return True


def random_event(player):
    events = [
        "gold",
        "healing",
        "nothing",
        "trap"
    ]

    event = random.choice(events)

    if event == "gold":
        amount = random.randint(5, 20)
        player.gold += amount
        print(f"\nYou find {amount} gold!")

    elif event == "healing":
        heal = random.randint(10, 25)
        player.health += heal
        print(f"\nYou recover {heal} health.")

    elif event == "trap":
        damage = random.randint(5, 15)
        player.health -= damage
        print(f"\nA trap hurts you for {damage} damage.")

    else:
        print("\nNothing unusual happens.")

WORLD = {

    "village": {
        "text":
        "You stand in the Village of Eldoria. "
        "Rumors speak of a Shadow Dragon.",
        "choices": {
            "1": ("Visit Forest", "forest"),
            "2": ("Visit Cave", "cave"),
            "3": ("Visit Castle", "castle")
        }
    },

    "forest": {
        "text":
        "Ancient trees surround you.",
        "choices": {
            "1": ("Search deeper", "deep_forest"),
            "2": ("Return", "village")
        }
    },

    "deep_forest": {
        "text":
        "You discover a glowing sword stuck in stone.",
        "choices": {
            "1": ("Take sword", "sword"),
            "2": ("Leave", "forest")
        }
    },

    "sword": {
        "text":
        "The sword pulses with magical energy.",
        "choices": {
            "1": ("Claim it", "claim_sword")
        }
    },

    "cave": {
        "text":
        "Darkness fills the cave.",
        "choices": {
            "1": ("Explore", "goblin"),
            "2": ("Return", "village")
        }
    },

    "castle": {
        "text":
        "The king seeks heroes.",
        "choices": {
            "1": ("Accept quest", "quest"),
            "2": ("Return", "village")
        }
    },

    "quest": {
        "text":
        "The king asks you to defeat the Shadow Dragon.",
        "choices": {
            "1": ("Begin journey", "mountains"),
            "2": ("Return", "village")
        }
    },

    "mountains": {
        "text":
        "The Dragon's mountain rises before you.",
        "choices": {
            "1": ("Climb", "dragon_gate"),
            "2": ("Return", "village")
        }
    },

    "dragon_gate": {
        "text":
        "A giant gate blocks the path.",
        "choices": {
            "1": ("Enter", "dragon")
        }
    }

}

def special_location(player, location):

    if location == "claim_sword":

        if "Dragon Slayer Sword" not in player.inventory:

            print("\nYou pull the legendary sword free!")

            player.inventory.append(
                "Dragon Slayer Sword"
            )

            player.attack += 10

            achievement(
                player,
                "Chosen Hero"
            )

        return "forest"

    if location == "goblin":

        win = battle(
            player,
            "Goblin",
            40,
            8
        )

        if not win:
            return "death"

        random_event(player)

        return "cave"

    if location == "dragon":

        dragon_hp = 150

        if "Dragon Slayer Sword" in player.inventory:
            dragon_hp = 100

        win = battle(
            player,
            "Shadow Dragon",
            dragon_hp,
            18
        )

        if not win:
            return "death"

        achievement(
            player,
            "Dragon Slayer"
        )

        return "victory"

    return location

def create_character():

    print("\n=== REALM OF INFINITE CHOICES ===\n")

    name = input("Enter your name: ")

    print("\nChoose a class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Rogue")

    choice = input("> ")

    classes = {
        "1": "Warrior",
        "2": "Mage",
        "3": "Rogue"
    }

    role = classes.get(choice, "Warrior")

    return Player(name, role)


def play(player, start_location):

    location = start_location

    while True:

        if player.health <= 0:
            location = "death"

        if location == "death":

            print("\n☠ GAME OVER")
            break

        if location == "victory":

            print("\n🐉 THE SHADOW DRAGON HAS FALLEN!")
            print("The kingdom is saved.")
            print("You become a legendary hero.")

            print("\nAchievements:")
            for a in player.achievements:
                print("-", a)

            break

        if location in WORLD:

            node = WORLD[location]

            print("\n" + "=" * 50)
            print(node["text"])

            player.show_stats()

            for key, value in node["choices"].items():
                print(f"{key}. {value[0]}")

            print("S. Save")
            print("Q. Quit")

            choice = input("\nChoice: ").upper()

            if choice == "S":
                save_game(player, location)
                continue

            if choice == "Q":
                break

            if choice in node["choices"]:

                location = node["choices"][choice][1]

                location = special_location(
                    player,
                    location
                )

            else:
                print("Invalid choice.")

        else:
            location = special_location(
                player,
                location
            )


def main():

    print("1. New Game")
    print("2. Load Game")

    option = input("> ")

    if option == "2":

        player, location = load_game()

        if player:
            play(player, location)
            return

        print("No save found.")

    player = create_character()

    play(player, "village")


main()
