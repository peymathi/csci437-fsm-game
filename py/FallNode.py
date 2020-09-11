from OneWayNode import OneWayNode

# Identical to the OneWayNode except that this node takes away some health from the user from the fall
class FallNode (OneWayNode):

    def __init__(self, player, nextNodes, message, options, fallDamage, enemy = None, item = None):
        super().__init__(player, nextNodes, message, options, enemy = None, item = None)

        self._fall_damage = fallDamage

    def _init_room(self):

        if self._fall_damage < 10:
            print("You fall through a hole in the floor to the next level down. You take 5 damage from this fall.")

        else:
            print("You fall through a hole in the floor to a couple levels down. You have an intense headache now and you lose 10 HP.")

        print(self._message)