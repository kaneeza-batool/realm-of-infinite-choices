# Realm of Infinite Choices

A terminal-based fantasy RPG built in Python. Choose your class, explore a branching world, battle enemies, collect items, and face the legendary Shadow Dragon. Features save/load support and an achievement system.

---

## Features

- 3 playable classes: Warrior, Mage, and Rogue, each with unique stats
- Branching world map with multiple locations to explore
- Turn-based battle system with attack and run options
- Random events: gold, healing, traps, or nothing
- Legendary item: Dragon Slayer Sword that reduces the final boss HP
- Achievement system that unlocks based on actions
- Save and load game progress via a JSON file
- Clean stat display after every move

---

## Project Structure

```
RealmOfInfiniteChoices/
├── game.py          # Main game file with all logic
└── savegame.json    # Auto-generated on save (not committed)
```

---

## Getting Started

1. Clone the repo
   ```bash
   git clone https://github.com/your-username/realm-of-infinite-choices.git
   cd realm-of-infinite-choices
   ```

2. Run the game
   ```bash
   python game.py
   ```

No external libraries required. Works with Python 3.6 and above.

---

## How to Play

1. Choose New Game or Load Game
2. Enter your character name and pick a class
3. Navigate the world by entering the number of your choice
4. Type `S` at any location to save your progress
5. Type `Q` to quit

### Controls

| Input | Action |
|-------|--------|
| `1`, `2`, `3` | Choose a path or option |
| `attack` | Attack during battle |
| `run` | Attempt to flee (50% chance) |
| `S` | Save game |
| `Q` | Quit game |

---

## Classes

| Class | HP | Attack | Starting Gold |
|-------|----|--------|---------------|
| Warrior | 120 | 15 | 20 |
| Mage | 80 | 25 | 30 |
| Rogue | 100 | 18 | 50 |

---

## World Map

```
Village of Eldoria
├── Forest
│   └── Deep Forest
│       └── Glowing Sword (claim it to get Dragon Slayer Sword)
├── Cave
│   └── Goblin Battle + Random Event
└── Castle
    └── King's Quest
        └── Mountains
            └── Dragon Gate
                └── Shadow Dragon (final boss)
```

---

## Achievements

| Achievement | How to Unlock |
|-------------|---------------|
| Chosen Hero | Pull the Dragon Slayer Sword from the stone |
| Dragon Slayer | Defeat the Shadow Dragon |

---

## Save System

Progress is saved to `savegame.json` in the same directory. It stores your name, class, health, attack, gold, inventory, achievements, and current location. The file is created automatically when you press `S` in-game.

It is recommended to add `savegame.json` to your `.gitignore` so personal save data is not committed:

```
# .gitignore
savegame.json
```

---

## Customization

### Add a new location
In `game.py`, add an entry to the `WORLD` dictionary:

```python
"swamp": {
    "text": "A murky swamp stretches before you.",
    "choices": {
        "1": ("Wade through", "swamp_monster"),
        "2": ("Turn back", "village")
    }
}
```

### Add a new enemy
Call the `battle()` function with your own enemy name, HP, and attack:

```python
win = battle(player, "Swamp Witch", 60, 12)
```

### Add a new achievement
Call `achievement()` anywhere in the code:

```python
achievement(player, "Swamp Survivor")
```

---

## Example Playthrough

```
1. New Game

=== REALM OF INFINITE CHOICES ===
Enter your name: Kaneeza
Choose a class:
1. Warrior
2. Mage
3. Rogue
> 2

You stand in the Village of Eldoria...
1. Visit Forest
2. Visit Cave
3. Visit Castle
S. Save
Q. Quit

Choice: 1
Ancient trees surround you...
```

---

## Author

**Kaneeza Batool**
CS Undergraduate, Sukkur, Pakistan
Built with Python
