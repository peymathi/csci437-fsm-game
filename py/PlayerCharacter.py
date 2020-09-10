from Character import Character
import math
from Die import Die

class PlayerCharacter (Character):

    def __init__(self, health, armor, damage):
        super().__init__(health, armor, damage, 1)
        self.__exp_needed = 2

    def attempt_flee(self):
        
        # Roll each die and if a 2 is rolled then return true
        for item in self._inventory:
            if isinstance(item, Die):
                if (item.roll() == 2):
                    return True
        return False

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