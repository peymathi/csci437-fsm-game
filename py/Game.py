from GraphBuilder import GraphBuilder
from Node import Node

class Game:
    
    def __init__(self):
        self._builder = GraphBuilder()

    # Build graph and evaluate the starting node
    def start(self):
        
        welcomeString = """
Welcome to Grool's Manor. You are an adventurer who enjoys traveling off the beaten path. While hiking
through the night, you see a shiny spirit humming in the distance. Intrigued, you follow the spirit. The spirit
seems to be singing a song which resonates with your soul. As you get closer you feel a vibration in your chest.
Eventually you arrive at what appears to be an old Victorian Manor. You briefly glance but don't get the best look at the place as you
begin following the sprit inside. As you walk up the front steps of the porch you begin to see the shimmering glow of rubies,
riches, and gold inside the manor! You quickly run inside and as you step through the door all of the light blinks to darkness
and you hear the door slam behind you. The sweet songs you heard before have turned to chilling screams which shake your bones.
You can barely see anything but you hear the groaning of damned souls all throughout the manor. You hear the faint laughter of a 
terrible sorcerer off in the distance. The sorcerer taunts you exclaiming "I am the sorcerer Grool! I have lured you into my trap, and 
now like many before you I will harvest your soul to become my slave forever!". What have you gotten yourself into?

...and how will you get out?\n
"""
        print(welcomeString)
        input("Press enter to start...")    

        # Loop until the player wins the game or quits
        while (True):

            # Build the level and start the game
            self._builder.build_graph()
            start = self._builder.get_start()

            result = start.evaluate()
            if result:
                self.end()
                break
    
    def end(self):
        pass


    