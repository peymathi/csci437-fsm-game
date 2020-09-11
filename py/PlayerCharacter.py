from Character import Character
from Die import Die
from StatItem import StatItem 

import math

class PlayerCharacter (Character):

    def __init__(self, health, armor, damage):
        super().__init__(health, armor, damage, 1)
        self.__exp_needed = 2

    def show_inventory(self):
        print("You open your satchel to find the following items:\n")
        for item in self._inventory:
            print(f"{item.getName()} - {item.getDescription()}")

    def get_exp(self):
        return self.__exp_needed

    def add_exp(self, amount):
        self.__exp_needed -= amount

        # Check if player has leveled up leveled up
        if self.__exp_needed < 1:

            # Set the next value for exp needed to level up. Next exp_needed value is determined by 2^current_level
            # unless the current level is greater than 6. After that point the next exp_needed value is determined by
            # 2^6 + 32 times however many levels past 6 the player is.
            temp = self.__exp_needed
            if self._level > 6:
                self.__exp_needed = math.pow(2, 6) + (self._level - 6) * 32
                self.__exp_needed += temp

            else:
                self.__exp_needed = math.pow(2, self._level)
                self.__exp_needed += temp
            
            self._level_up()

    def _level_up(self):
        
        # Loop until user picks an attribute
        while(True):
            print("You've leveled up! Select an attribute to add a point into: ")
            print("\t(h)ealth\t(a)rmor\t(d)amage\n")

            userInput = input("User Input: ")
            userInput = userInput.upper().strip()

            if userInput in {'H', 'HP', 'HEALTH'}:
                self._max_health += 1
                break

            elif userInput in {'A', 'ARMOR'}:
                self._armor += 1
                break

            elif userInput in {'D', 'DAMAGE'}:
                self._damage += 1

            else:
                print ("\nInvalid User Input")

            # Refill HP on level up
            self._health = self._max_health

    def generate_attack(self):

        # Go through each item in inventory and if its a die roll it and add to list of rolled dice. Select max.
        vals = []
        for item in self._inventory:
            if isinstance(item, Die):
                vals.append(item.roll())

        print(f"You rolled the following values: {vals}")
        attack = max(vals)
        return attack * self._damage

    # Remove player's inventory and refill health
    def _die(self):
        
        # Remove stat bonuses
        for item in self._inventory:
            if isinstance(item, StatItem):
                self._max_health -= item.health()
                self._armor -= item.armor()
                self._damage -= item.damage()

        # Clear inventory
        self._inventory = []
        self._health = self._max_health

        # Display death message
        print(
"""You have been slain... Grool has feasted on your body and reanimated all of the beasts you had killed.
The items you had collected have been returned to their original places, but your soul has been transferred
from your old body to a new adventurer entering the manor. With your soul you bring with you all raw stats
that you had prior to your death (no bonus stats from items).
""")

        print(
f"""\nYou are still Level {self._level}, your Max HP is still {self._max_health}, your Armor Level is still {self._armor}, 
and your Damage Level is still {self._damage}. Pick yourself up, and venture onwards to defeat Grool!
""")

