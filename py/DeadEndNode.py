from CommonNode import CommonNode

class DeadEndNode (CommonNode):

    def __init__(self, player, exit, message, enemy = None, item = None):
        super().__init__(player, [], message, [], enemy, item)

        self._exit = exit

    def _choose_next(self):

        # Loop until the user leaves the node
        while True:

            print("What would you like to do?\n")

            print("(V)iew Player Stats \t (G)o Back\n")

            # Get user input and determine next node
            userInput = input("User Input: ")
            userInput = userInput.upper().strip()

            # Evaluate next node
            if userInput in {'V', 'VIEW', 'VIEW PLAYER STATS', 'VIEW STATS'}:
                    self._player.show_inventory()

            elif userInput in {'G', 'GO', 'GO BACK'}:
                return self._exit.evaluate(self)
