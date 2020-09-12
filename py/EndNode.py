from CommonNode import CommonNode

# The last node of the games. It's evaluate method is pretty much the same, but returns True when the enemy is killed
# so that the game ends.
class EndNode (CommonNode):

    def _choose_next(self):
        print("You have defeated Grool and freed all of the damned spirits under his control.")
        print("The light shines brightly on your heroic soul. Go now and enjoy the gold and glory you have earned.")
        return True
