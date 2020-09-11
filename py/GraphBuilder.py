from Node import Node
from Die import Die
from StatItem import StatItem
from EnemyCharacter import EnemyCharacter
from CommonNode import CommonNode
from OneWayNode import OneWayNode
from DeadEndNode import DeadEndNode
from FallNode import FallNode
from PlayerCharacter import PlayerCharacter

class GraphBuilder:

    def __init__(self):
        
        self._start_node = None

    def build_graph(self):
        
        # Build some items
        foundStat = StatItem('Found Stat Item', 'Big Blade', 0, 5, 0)
        droppedStat = StatItem('Dropped Stat Item', 'Blocks damage', 3, 0, 0)
        monsterDie = Die('Monster Die', 'Monster Die', [1, 2, 4])
        droppedDie = Die('Dropped Die', 'Dropped Die', [2, 3, 4])
        foundDie = Die('Found Die', 'Found Die', [5, 6, 7])
        coin = Die('Coin', 'Coin', [1, 2])

        # Build a player
        player = PlayerCharacter(50, 5, 5)

        # Build some enemies
        # (name, health, armor, damage, )
        enemy1 = EnemyCharacter("No Item", 10, 2, 3, 3, None, 5, False)
        enemy1.add_item(monsterDie)

        enemy2 = EnemyCharacter("Drops Die", 10, 2, 3, 3, droppedDie, 5, False)
        enemy2.add_item(monsterDie)
        enemy2.add_item(droppedDie)

        enemy3 = EnemyCharacter("Drops Stat Item", 10, 2, 3, 3, droppedStat, 5, False)
        enemy3.add_item(droppedStat)

        # Build the nodes
        start = CommonNode(player, [], "Welcome to Groo's Manor.", [], None, coin)

        node2 = CommonNode(player, [start], "You are now in a large hallway.", ['Go through the south door'], enemy1, foundStat)
        start.add_node(node2, 'Go through the north door')

        node3 = CommonNode(player, [start], 'You are now in a small parlor with a piano in the corner.', ['Go through the west door'], enemy2)
        start.add_node(node3, 'Go through the east door')

        node4 = CommonNode(player, [start], 'You are now in a bathroom', ['Go through the east door'], enemy3, foundDie)
        start.add_node(node4, 'Go through the west door')

        # Link them together

        # Call eval on start node
        result = start.evaluate()
        if result:
            print("Player Won")
        else:
            print("Player lost")

if __name__ == '__main__':
    builder = GraphBuilder()
    builder.build_graph()
