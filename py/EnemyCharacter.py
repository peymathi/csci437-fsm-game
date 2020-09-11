from Character import Character
from Item import Item

class EnemyCharacter (Character):

    def __init__(self, name, health, armor, damage, level, item, exp, first):
        super().__init__(health, armor, damage, level)
        
        # Item given to the player on death
        self._item_to_drop = item

        # Bool to determine if the enemy will surprise attack
        self._attacks_first = first
        
        # Amount of exp that the player will get on death
        self._exp = exp

        self._name = name

        # Various messages that the enemy will display
        self._attack_msg = ''
        self._flee_block_msg = ''
        self._death_msg = ''
    
    def getExp(self):
        return self._exp

    def getName(self):
        return self._name

    def attacksFirst(self):
        return self._attacks_first

    def setAttack(self, msg):
        self._attack_msg = msg

    def setFlee(self, msg):
        self._flee_block_msg = msg

    def setDeath(self, msg):
        self._death_msg = msg

    def getAttack(self):
        return self._attack_msg

    def getFlee(self):
        return self._flee_block_msg

    def getDeath(self):
        return self._death_msg
    
    def getItem(self):
        return self._item_to_drop

    def _die(self):
        return False