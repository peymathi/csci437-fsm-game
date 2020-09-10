from Character import Character
from Item import Item

class Node:

    def __init__(self, nextNodes: list = [], enemy: Character = None, message: str = '', options: tuple = ({'Do nothing'} * 5), item: Item = None):

        # List of the nodes that could potentially be next
        self._nextNodes = []

        # Enemy character for the node if there is one. 
        self._enemy = None

        # Message that will greet the user as they enter the room
        self._message = message

        # Messages for each option that the user can select
        self._options = options

        # Item that the room can contain
        self._item = item

    # Displays the message for the given node.
    def prompt_message(self):
        print(self._message)
    
    # Loop for the node. Could have many moving parts, boss fight, event, etc. Overall just somehow returns the next node
    def evaluate(self):
        pass

# Testing
if __name__ == "__main__":
    pass
