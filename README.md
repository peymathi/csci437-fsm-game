# Finite State Machine Game: Grool's Manor

Grool's Manor is a text-based game driven by a finite state machine. The game is defined by a finite state machine where each state in the machine represents a location that the player can be in the Manor which is the game's playing area. The transitions between states are represented by different actions that the player can take within each room. These transitions could be opening a door, walking up a staircase, walking down a hallway, and many more. The machine has a starting state at the entrance of the Manor, and one final state after the final boss is created. If the machine halts in the final state, then the player has beaten the game. Otherwise if the machine haults in a non-final state, then the player has died and must restart the game. The game also has combat and progression systems, but those aspects of the game are completely unrelated to the finite state machine driven design.


## Instructions to play:
<hr>

### On IUPUI Tesla Shared Server:
<br>

```
cd /home/peymathi/gamedev/grools-manor/

./grools-manor
```

### Other
<br>

```
git clone https://github.com/peymathi/csci437-fsm-game.git

cd csci437-fsm-game.git

./grools-manor
```

## Game Aspects
<hr>

Below are various aspects and systems of the game's top level design:

- **Combat System:** The combat system is turn based and built around dice rolling. Players have a base damage value which is then multiplied by the number rolled on the dice to produce the amount of damage done. There are more complicated aspects of the combat system including armor values and critical strikes which are explained later

- **Player Stats:** The player has a set of raw stats that affect combat. These stats are increased through leveling up in a hidden EXP system. EXP is gained by the player by defeating enemies. The stats that the player has are HP, Armor, and DMG. HP is how much health the player has. Armor reduces the amount of damage that an enemies attack does. DMG is the raw damage value that is used to determine how much damage the player does on an attack. The player also has a LVL attribute, but that does not affect combat and only serves to give the player a general sense of how strong they are compared to enemies. All of these stats are also shared by monsters fought in the game. Each monster will have HP, Armor, DMG, and LVL attributes which are visible to the player. Leveling up also refills the player's health.

- **Items / Inventory:** The player has an infinite inventory to collect items found in the game. This means that the player can potentially hold every item in the game at one time. Items do various things such as increasing base stats, unlocking areas, and more. Items cannot be dropped, as there is no reason to drop an item.

- **Dice:** The player starts with a die only containing 2 numbers: 1 and 2 (called coin). Over the course of the game the player can find more dice which can have different ranges of possible numbers and probabilities. When entering combat, all of the dice that the player currently has will be rolled and whichever die gives the highest result will be chosen to calculate the player's damage for that attack.

- **Critical Strikes:** The player can perform a critical strike on an enemy by rolling a ten on any of the dice rolled. In this case, the player will deal 40% of the enemy's missing health OR normal damage depending on which is higher.

- **Player Death:** On death, the finite state machine is completely reset putting the player at the beginning of the game. In other words, the entire state of the game is set back to the game's start. All items, monsters, an doors are reset. The only thing that is kept on reset is the player's stats.

<br>

## Misc Parts of the Game
<hr>

- Enemies only respawn on death.
- Some areas of the level allow the player to restore their HP to full.
- On any given turn, the player can choose to attempt to flee. In this case, all dice are rolled and if one of the dice comes up as a 2 then the player will successfully flee. Otherwise they forfeit their turn and the fight continues.

<br>

## Object Oriented Design
<hr>
I chose to develop Grool's Manor using Object Oriented Design in Python for a few reasons. The first being that it is a comfort tool for me to use OOD and Python. The second being the extendability of OOD allowing me to potentially expand upon this game in the future. The final reason is that employers want to see OOD in projects of their candidates, and using it in this project allows me to showcase my OOD skills on my GitHub.

<br/>Below is a brief description of some of the classes in order to showcase the OOD used in the game.

### Character Class:
- Tracks all combat data relating to any entity in the game that can fight. Including players and enemies.
- Abstract class
- EnemyCharacter and PlayerCharacter inherit from Character
- Has methods for the character to generate an attack and receive an attack

### Node Class
- Represents a Node in the graph, or a state in the finite state machine
- Each node is a room in the level.
- Abstract class
- Node contains a reference to the player, a list of possible nodes the player could go to next, and list of options messages
- Every Node has an evaluate() method which is the gameplay loop that happens from the moment the player enters a node, to eventually selecting a new node for the player to go to (or player dies / wins game)
- Several different Node types implement the Node class including CommonNode 

### Item Class
- Represents an item in the game that can go into a character's inventory
- Base class only has a name and a description
- Die and StatItem inherit from this class
- Die class represents a die that can be rolled. Has a set of numbers that are possible
- StatItem class represents an item that a character can hold to boost their raw stats

### Battle Class
- Battle class represents a battle between the player character and an enemy character
- The battle class is essentially a stateful function
- The battle class has a method called start_battle() that starts the battle and runs until the battle is ended in one of three different ways: player dies, enemy dies, or player flees.
- The result of the battle is stored as a member of the class and can be retrieved from the battle instance at the conclusion of the start_battle() method

<br>

## Lessons Learned
<hr>
