from Character import Character
from Item import Item

class EnemyCharacter (Character):

    def __init__(self, health, armor, damage, level, item):
        super().__init__(health, armor, damage, level)
        
        # Item given to the player on death
        self._item_to_drop = item

    def get_item(self):
        return self._item_to_drop