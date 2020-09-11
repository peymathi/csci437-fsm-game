from Character import Character
from Item import Item

class EnemyCharacter (Character):

    def __init__(self, name, health, armor, damage, level, item, first):
        super().__init__(health, armor, damage, level)
        
        # Item given to the player on death
        self._name = name
        self._item_to_drop = item
        self._attacks_first = first

        self._attack_msg = ''
        self._flee_block_msg = ''
        self._death_msg = ''

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