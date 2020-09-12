from Node import Node
from Die import Die
from StatItem import StatItem
from EnemyCharacter import EnemyCharacter
from CommonNode import CommonNode
from FallNode import FallNode
from PlayerCharacter import PlayerCharacter

class GraphBuilder:

    def __init__(self, player):
        
        self._start_node = None
        self._player = PlayerCharacter(5, 0, 1)

    def get_start(self):
        return self._start_node

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
        start = CommonNode(player, "Welcome to Grool's Manor.", None, coin)

        node2 = CommonNode(player, "You are now in a large hallway.", enemy1, foundStat)

        node3 = CommonNode(player, 'You are now in a small parlor with a piano in the corner.', enemy2)

        node4 = CommonNode(player, 'You are now in a bathroom', enemy3, foundDie)
        

        # Link them together
        start.add_node(node3, 'Go through the east door')
        start.add_node(node2, 'Go through the north door')
        start.add_node(node4, 'Go through the west door')

        node2.add_node(start, 'Go through the South door')
        node3.add_node(start, 'Go through the West door')
        node4.add_node(start, 'Go through the East door')

        self._start_node = start
        # Call eval on start node
        # result = start.evaluate()
        # if result:
        #     print("Player Won")
        # else:
        #     print("Player lost")

if __name__ == '__main__':
    builder = GraphBuilder()
    builder.build_graph()
