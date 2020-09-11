from CommonNode import CommonNode

# Exactly like a CommonNode, but overrides the method choosing the next node and does not allow the user to go back
class OneWayNode (CommonNode):

    def choose_next(self):
        pass