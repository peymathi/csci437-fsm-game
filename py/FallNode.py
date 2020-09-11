from OneWayNode import OneWayNode

# Identical to the OneWayNode except that this node takes away some health from the user from the fall
# and then immediately sends the player to another node
class FallNode (OneWayNode):

    def __init__(self, player, fallDamage, nextNode):
        super().__init__(player, [], '', [], None, None)
        self._next_node = nextNode
        self._fall_damage = fallDamage

    def _init_room(self):

        if self._fall_damage < 10:
            print("You fall through a hole in the floor to the next level down. You take 5 damage from this fall.")

        else:
            print("You fall through a hole in the floor to a couple levels down. You have an intense headache now and you lose 10 HP.")

        