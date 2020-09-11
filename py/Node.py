from PlayerCharacter import PlayerCharacter
from Battle import Battle

# Abstract class
class Node:

    def __init__(self, player: PlayerCharacter, nextNodes: list = [], message: str = '', options: tuple = (['Do nothing'] * 5)):

        # Reference to the player character
        self._player = player
        
        # List of the nodes that could potentially be next
        self._next_nodes = []

        # Message that will greet the user as they enter the room
        self._message = message

        # Messages for each option that the user can select. Index of the option in the list should match with the
        # index for the node to visit in _nextNodes
        self._options = options
    
    # Loop for the node. Could have many moving parts, boss fight, event, etc. Overall just somehow calls the
    # evaluate method for the next node.
    # Returns false if the player has died. Returns true if the player wins the game.
    # Takes a reference to the last node the player was at.
    # Abstract method
    def evaluate(self, prevNode: Node = None):
        raise Exception("Abstract method evaluate() called on Node class")
