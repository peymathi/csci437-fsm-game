from Node import Node
from Die import Die
from StatItem import StatItem
from EnemyCharacter import EnemyCharacter
from CommonNode import CommonNode
from FallNode import FallNode
from PlayerCharacter import PlayerCharacter
from EndNode import EndNode

class GraphBuilder:

    def __init__(self):
        
        self._start_node = None
        self._player = PlayerCharacter(20, 0, 1)

    def get_start(self):
        return self._start_node

    def build_graph(self):
        
        # Build some items
        monsterDie = Die('Monster Die', 'Common die that monsters use.', [1, 2, 4])
        coin = Die('Coin', "A penny. Maybe it's lucky and it will help you escape? Worst die in the game either way.", [1, 2])
        stick = StatItem("Stick", "It's literally just a stick... better than using my fists I guess.", 0, 2, 0)
        samuraiSword = StatItem('Samurai Sword', 'Badass looking sword. Might be a bit dull though.', 0, 2, 0)
        doransShield = StatItem('Shield of Doran', "Dinky little wooden shield. Doesn't make you feel much safer.", 3, 0, 1)
        ring = StatItem("Lover's Lost Ring", "A beatiful engagement ring. Infused with true love. Does wearing this even help me at all?", 0, 1, 5)
        cloak = StatItem("Cloak of the Divine", "Putting it on makes your body feel rejuvinated. You feel like you could run a marathon now.", 3, 0, 20)
        knightsVeil = StatItem("Knight's Veil", "Feels harder than steel. Could probably block bullets and swords alike.", 15, 0, 3)
        muramasa = StatItem("Muramasa", "An ancient sword engraved with its name. It hums in your hand as you unsheathe it.", 0, 5, 0)
        devilsDice = Die("Devil's Dice", "Ordinary set of craps dice, except they were used by the Devil to gamble souls with.", [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
        critical = Die("Critical", "This die is completely hit or miss", [2, 10])

        # Build some enemies
        # (name, health, armor, damage, )
        grool = EnemyCharacter('Sorcerer Grool', 100, 30, 20, 130, None, 0, False)
        zombie = EnemyCharacter('Zombie', 4, 0, 1, 1, None, 2, False)
        piano = EnemyCharacter('Grand Piano', 10, 1, 5, 5, monsterDie, 10, True)
        demon = EnemyCharacter("Demon King", 5, 5, 10, 8, None, 18, False)
        skeleton = EnemyCharacter("Skeleton", 5, 0, 5, 4, doransShield, 8, True)
        wolves = EnemyCharacter("Pack of Wolves", 20, 0, 3, 7, None, 12, True)
        executioner = EnemyCharacter("Executioner", 30, 20, 20, 30, knightsVeil, 64, False)
        giantSpider = EnemyCharacter("Giant Spider", 35, 10, 7, 30, None, 64, False)
        baronNashor = EnemyCharacter("Baron Nashor (Giant Worm)", 50, 20, 10, 100, muramasa, 200, False)
        dragon = EnemyCharacter("Fire Breathing Dragon", 30, 10, 20, 100, None, 200, False)

        # Give enemies dice
        grool.add_item(monsterDie)
        zombie.add_item(monsterDie)
        piano.add_item(monsterDie)
        demon.add_item(monsterDie)
        skeleton.add_item(monsterDie)
        wolves.add_item(monsterDie)
        executioner.add_item(monsterDie)
        giantSpider.add_item(monsterDie)
        baronNashor.add_item(monsterDie)
        dragon.add_item(monsterDie)

        
        # give enemies attack, flee, and death messages
        grool.setAttack("steals your life essence from you")
        zombie.setAttack("bites some of your flesh off")
        piano.setAttack("slams its lid shut on your head")
        demon.setAttack("curses you")
        skeleton.setAttack("swings its arm like a club at you")
        wolves.setAttack("circle you and tackle you to the ground")
        executioner.setAttack("strikes you with his axe")
        giantSpider.setAttack("slows you with her web and injects poison into you")
        baronNashor.setAttack("spits pools of venom at your burning your legs")
        dragon.setAttack("blows fireballs at you")

        grool.setFlee("slams the door shut behind you.")
        zombie.setFlee("trips you and pulls you back.")
        piano.setFlee("plays a melody which mesmerizes you back to the battle.")
        demon.setFlee("offers you a deal you cannot refuse.")
        skeleton.setFlee("throws its arm at you, tripping you in the process and pulling you back.")
        wolves.setFlee("run around you to block your exit.")
        executioner.setFlee("piles his dead bodies at the door blocking your exit.")
        giantSpider.setFlee("builds a web blocking the door.")
        baronNashor.setFlee("burrows under the floor and springs up blocking your path.")
        dragon.setFlee("blows a fireball creating a massive fire in front of the door blocking your exit.")

        grool.setDeath("screams in terror as he is dragged to the shadow realm hell of his dimension.")
        zombie.setDeath("explodes in blood and guts.")
        piano.setDeath("plays a sad tune and falls apart.")
        demon.setDeath("flees in terror back to hell.")
        skeleton.setDeath("crumbles into a pile of bones.")
        wolves.setDeath("run away to lick their wounds whining like hurt puppies.")
        executioner.setDeath("prepares the guillotine to put himself out of his misery.")
        giantSpider.setDeath("withers and bleeds out from her wounds.")
        baronNashor.setDeath("wails in pain as he shrivels to the size of a maggot.")
        dragon.setDeath("slowly burns away into a pile of ash.")

        # Build the nodes
        start = CommonNode(self._player, "Welcome to Grool's Manor. It is almost pitch black, but you can barely make out three doors.", None, coin)
        first = CommonNode(self._player, "You enter what appears to be a small parlor.", zombie, None)
        second = CommonNode(self._player, "You look around in a dark room. There is a grand piano in the corner that appears to be playing music.", piano, None)
        third = CommonNode(self._player, "You enter... well you don't really know what you've entered. It seems like you're back in the woods again. What is this place? It might be some kind of courtyard, but you can't see the sky.", wolves, None)

        firstSecond = CommonNode(self._player, "You enter a small closet. Seems like it is pretty much empty except for this stick on the ground.", None, stick)
        secondSecond = CommonNode(self._player, "You enter what looks to be a kitchen.", skeleton, None)
        thirdSecond = CommonNode(self._player, "You head upstairs and into a room lit by red candle light. You smell blood and you see a pentagram in the middle with a ram's head in the center.", demon, samuraiSword)

        secondThird = CommonNode(self._player, "You head upstairs and immediately vomit as you enter this room. What could that smell be? Then you see them. All the dead bodies. You strangely hear a crowd cheering, but no one is in sight.", executioner, None)
        thirdThird = CommonNode(self._player, "You see a HUGE spider in the doorway as you enter the room. Definitely the biggest you've ever seen- oh god.. what is that monstrocity in the center of the room...", giantSpider, cloak)

        secondBalcony = CommonNode(self._player, "You step out onto a balcony. For once you can actually see the outside world. It's actually beautiful out here. The full moon looks so pretty tonight. If only you weren't in this nightmare you could enjoy it. You look down and realize it is way too high up to jump down, but there's something else on the ground here. You pick up something shiny.", None, ring)
        thirdFall = FallNode(self._player, "You open the door and step inside a pitch black room. You take a couple steps forward and suddenly fall two the floor below!", 10, first)

        secondFourth = CommonNode(self._player, "You smell a putrid foul stench as you enter the room. You look up and see a giant 9-eyed worm staring down at you dripping puss from its fangs.", baronNashor, None)
        thirdFourth = CommonNode(self._player, "You put your hand on the doorknob and burn it. What could be behind the door? You kick the door down and immediately feel the heat of the fire breathing dragon standing before you.", dragon, devilsDice)

        preboss = CommonNode(self._player, "You cautiously step into room with your shield up and weapons drawn. To your surprise there is nothing but a small fountain here. There isn't any water flowing and there is a small plaque on the front of the fountain. How strange. What was supposed to be here? You hear the sorcerer Grool laughing loudly nearby.", None, critical)

        boss = EndNode(self._player, "You enter a room with purple carpet and green flames at the edges of the room. Grool is turned with his back to you looking down at an alter. He's still laughing... you take two steps near him and he turns around revealing his burning orange eyes. You pull out your dice, ready to defeat Grool.", grool)

        # Link them together
        start.add_node(first, 'Enter the door to the East.')
        start.add_node(second, 'Enter the door to the West.')
        start.add_node(third, 'Enter the door to the South.')

        first.add_node(start, 'Enter the door to the West.')
        first.add_node(firstSecond, 'Enter the door to the South.')
        
        second.add_node(start, 'Enter the door to the East.')
        second.add_node(secondSecond, 'Enter the door to the South.')
        
        third.add_node(start, 'Enter the door to the North.')
        third.add_node(thirdSecond, 'Enter the door to the South.')

        firstSecond.add_node(first, 'Leave the closet')

        secondSecond.add_node(second, 'Enter the door to the North.')
        secondSecond.add_node(secondThird, 'Enter the door to the West.')

        thirdSecond.add_node(third, 'Enter the door to the North.')
        thirdSecond.add_node(thirdThird, 'Enter the door to the East.')
        thirdSecond.add_node(thirdFourth, 'Enter the door to the South.')

        secondThird.add_node(secondBalcony, 'Enter the door to the West.')
        secondThird.add_node(secondSecond, 'Enter the door to the East.')
        secondThird.add_node(secondFourth, 'Enter the door to the South.')

        thirdThird.add_node(thirdSecond, 'Enter the door to the West.')
        thirdThird.add_node(thirdFall, 'Enter the door to the North.')

        secondFourth.add_node(secondThird, 'Enter the door to the North.')
        secondFourth.add_node(preboss, 'Enter the door to the East.')

        thirdFourth.add_node(thirdSecond, 'Enter the door to the North.')
        thirdFourth.add_node(preboss, 'Enter the door to the West.')

        preboss.add_node(secondFourth, 'Enter the door to the West.')
        preboss.add_node(thirdFourth, 'Enter the door to the East.')
        preboss.add_node(boss, 'Enter the door to the South.')

        self._start_node = start

if __name__ == '__main__':
    builder = GraphBuilder()
    builder.build_graph()
