from PlayerCharacter import PlayerCharacter

# Abstract class
class Node:

    def __init__(self, player: PlayerCharacter, nextNodes: list = [], message: str = '', options: tuple = (['Do nothing'] * 5)):

        # Reference to the player character
        self._player = player
        
        # List of the nodes that could potentially be next
        self._nextNodes = []

        # Message that will greet the user as they enter the room
        self._message = message

        # Messages for each option that the user can select
        self._options = options
    
    # Loop for the node. Could have many moving parts, boss fight, event, etc. Overall just somehow calls the
    # evaluate method for the next node.
    # Returns false if the player has died. Returns true if the player wins the game.
    # Abstract method
    def evaluate(self):
        raise Exception("Abstract method evaluate() called on Node class")
