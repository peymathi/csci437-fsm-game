from CommonNode import CommonNode

# Temporary node that makes the player take damage first before going on to the nextNode
class FallNode (CommonNode):

    def __init__(self, player, message, fallDamage, nextNode):
        super().__init__(player, message)
        self._next_node = nextNode
        self._fall_damage = fallDamage

    def _init_room(self):
        print(f"{self._message} taking {self._fall_damage} damage.")
        return self._next_node.evaluate()
        