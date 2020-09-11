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

    def get_armor(self):
        return self._armor

    def get_health(self):
        return self._health

    def get_max_health(self):
        return self._max_health

    def get_damage(self):
        return self._damage

    def get_level(self):
        return self._level

    # Returns false if dead and true if still alive
    def receive_attack(self, attack):
        attack = attack - self._armor
        if attack < 0:
            attack = 0
        self._health -= attack
        if self._health < 1:
            self._die()
            return False
        return True

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

        return vals

    # Abstract method
    def _die(self):
        raise Exception("Abstract method _die() called on Character class")