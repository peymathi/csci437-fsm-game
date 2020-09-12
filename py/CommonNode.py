from Node import Node
from EnemyCharacter import EnemyCharacter
from Item import Item
from Battle import Battle

# Node representing the common formula for a Node. Almost every Node be an instance of this class or derive from this class
class CommonNode (Node):

    def __init__(self, player, message, enemy = None, item = None):
        super().__init__(player, message)

        # Item found in the room
        self._item = item

        # Enemy encountered in the room
        self._enemy = enemy

        # Variables to track the state of the battle
        self._has_fleed = False
        self._has_lost = False

        # Previous node
        self._prev_node = None

    def evaluate(self, prevNode: Node = None):
        
        self._prev_node = prevNode

        # Modularization of this method into different methods to allow subclasses of this class to
        # customize individual parts of this method
        self._init_room()
        self._encounter_enemy()
        if (self._has_fleed):
            return self._prev_node.evaluate(self)
        elif (self._has_lost):
            return False    
        self._give_item()
        return self._choose_next()

    def _init_room(self):
        print(self._message)

    def _give_item(self):

        # If there is an item, give it to the player
        if self._item is not None:
            self._player.add_item(self._item)
            self._item = None

    def _encounter_enemy(self):

        # If there is an enemy, start the battle with it
        if self._enemy is not None:

            battle = Battle(self._player, self._enemy)
            battle.start_battle()

            if battle.fleed():
                
                # Go back to the previous node
                print("You frantically run back to the last room you were in.")
                self._has_fleed = True

            elif battle.won():
                self._enemy = None

            elif battle.lost():
                self._has_lost = True

    def _choose_next(self):
        
        # Loop until the user leaves the node
        while True:

            print("What would you like to do?\n")

            # Give the options
            print("", end='\t ')
            for i in range(len(self._options)):
                print(f"{i+1}){self._options[i]}", end=' \t ')

            print("(V)iew Player Stats \t (G)o Back\n")

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

                elif userInput in {'G', 'GO', 'GO BACK'}:
                    if self._prev_node is not None:
                        return self._prev_node.evaluate(self)
                    else:
                        print("You cannot go back here.")

