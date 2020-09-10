from Die import Die
from StatItem import StatItem

class Character:
    
    def __init__(self, health, armor, damage, level):
        
        self._max_health = health
        self._health = self._max_health
        self._armor = armor
        self._damage = damage
        self._level = level
        self._inventory = []

    def receive_attack(self, attack):
        self._health -= attack - self._armor
        if self._health < 1:
            self._die()

    def add_item(self, item):

        # Add stats to character if necessary
        if isinstance(item, StatItem):
            self._max_health += item.health()
            self._armor += item.armor()
            self._damage += item.damage()

        self._inventory.append(item)
        
    def generate_attack(self):

        # Go through each item in inventory and if its a die roll it and add to list of rolled dice. Select max.
        vals = []
        for item in self._inventory:
            if isinstance(item, Die):
                vals.append(item.roll())

        return max(vals)

    # Abstract method
    def _die(self):
        print("ERROR! This character doesn't know how to DIE!")