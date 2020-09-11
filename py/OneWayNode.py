from CommonNode import CommonNode

# Exactly like a CommonNode, but overrides the method choosing the next node and does not allow the user to go back
class OneWayNode (CommonNode):

    def choose_next(self):
        
        # Loop until the user selects an option
        while True:

            print("What would you like to do?\n")

            # Give the options
            print("", end='\t ')
            for i in range(len(self._options)):
                print(f"{i+1}){self._options[i]}", end=' \t ')

            print("(V)iew Player Stats\n")

            # Get user input and determine next node
            userInput = input("User Input: ")
            userInput = userInput.upper().strip()

            # Evaluate next node
            try:
                userInput = int(userInput)
                userInput -= 1
                return self._next_nodes[userInput].evaluate(self)

            except KeyboardInterrupt:
                raise KeyboardInterrupt

            except:
                if userInput in {'V', 'VIEW', 'VIEW PLAYER STATS', 'VIEW STATS'}:
                    self._player.show_inventory()