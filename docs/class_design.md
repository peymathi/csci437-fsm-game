# Class Structure for Grool's Manor

### Node Class
This class represents a node / state / location within the game. The node class can be overridden to allow for different types of nodes. The parent node class has the following properties:

- evaluate() method which represents the entire process of entering the state that the node represents, finishing any gameplay actions, and determining the next node to go to. Returns the next node.

<hr>

### Game Class
This class contains all of the properties of the game as a whole. Everything should be "global" in a sense goes here. The logical game loop is started here and all of the major moving pieces of the game are tracked here.

<hr>

### Character Class
This class represents any entity be it the player, monster, boss, enemy, etc that can engage in a fight. The class contains all of the properties and statistics that a fighting character will have such as HP, Armor, DMG, and LVL. This class also contains the character's inventory. Methods include attempting to flee, generating an attack, and receiving an attack.