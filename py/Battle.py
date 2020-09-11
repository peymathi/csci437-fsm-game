from PlayerCharacter import PlayerCharacter
from EnemyCharacter import EnemyCharacter
from StatItem import StatItem
from Die import Die

# Class that represents a battle. Essentially a function with state.
class Battle:

    def __init__(self, player, enemy):
        self._player = player
        self._enemy = enemy

        # Set at conclusion of battle to represent the result
        self._won = False
        self._lost = False
        self._fleed = False

        self._enemy_name = self._enemy.getName()

    def won(self):
        return self._won

    def lost(self):
        return self._lost

    def fleed(self):
        return self._fleed

    def start_battle(self):

        # Check if this enemy gets to attack first
        if self._enemy.attacksFirst():
            print("Surprise Attack!")
            attack = self._enemy.generate_attack()
            temp = (attack - self._player.get_armor())
            if temp < 0:
                temp = 0
            print(f"A {self._enemy_name} {self._enemy.getAttack()} dealing {temp} damage!")
            
            # Check if the player died
            lived = self._player.receive_attack(attack)
            if not lived:
                self._lost = True
                return

            print(f"You are now at {self._player.get_health()} HP.")

        # Loop until battle is over
        keepGoing = True
        while keepGoing:
            
            # Player move
            # Loop until user chooses move
            while True:
                
                print("It is your move. What would you like to do?")
                print("(A)ttack \t (I)nspect Enemy \t (F)lee \t (V)iew Inventory")
                userInput = input("\nUser Input: ")
                userInput = userInput.upper().strip()

                if userInput in {'A', 'ATTACK'}:
                    attack = self._player.generate_attack()
                    temp = (attack - self._enemy.get_armor())
                    if temp < 0:
                        temp = 0
                    print(f"Your attack does {temp} damage to the {self._enemy_name}.")
                    
                    # Check if the enemy died
                    lived = self._enemy.receive_attack(attack)
                    if not lived:
                        print(f"The {self._enemy_name} {self._enemy.getDeath()}.\n")
                        self._player.add_exp(self._enemy.getExp())
                        self._won = True
                        keepGoing = False
                    else:
                        print(f"The {self._enemy_name} is now at {self._enemy.get_health()} HP.")
                    print()
                    break
                    
                elif userInput in {'F', 'FLEE'}:
                    vals = self._player.generate_attack()
                    print("You attempt to flee by trying to roll a 2.")
                    print(f"You throw your dice hoping for the best and end up with {[i for i in vals]} values with your dice.")
                    
                    # If the player successfully fleed
                    if 2 in vals:
                        print("You get lucky with a 2 and successfully flee.\n")
                        self._fleed = True
                        keepGoing = False
                        break

                    else:
                        print(f"Despite your best efforts, a 2 was not found among your dice rolls. The {self._enemy_name} {self._enemy.getFlee()}.")
                        print()
                    break

                elif userInput in {'V', 'VIEW', 'VIEW INVENTORY'}:
                    self._player.show_inventory()
                    print()
                
                elif userInput in {'I', 'INSPECT', 'INSPECT ENEMY'}:
                    print(f"You are fighting what appears to be a {self._enemy_name}.")
                    print(f"The {self._enemy_name} has {self._enemy.get_health()} HP, {self._enemy.get_armor()} Armor, {self._enemy.get_damage()} Damage, and is Level {self._enemy.get_level()}.")
                    print()

                else:
                    print("I don't know what you want to do...\n")

            # Check if player move ended the battle
            if not keepGoing:
                break

            # Enemy move
            attack = self._enemy.generate_attack()
            temp = (attack - self._player.get_armor())
            if temp < 0:
                temp = 0
            print(f"The {self._enemy_name} {self._enemy.getAttack()} dealing {temp} damage!")
            
            # Check if the player died
            lived = self._player.receive_attack(attack)
            if not lived:
                self._lost = True
                return

            print(f"You are now at {self._player.get_health()} HP.\n")

# Testing
if __name__ == '__main__':

    # Make items
    die1 = Die('Coin', 'Your lucky penny. Can only roll values 1 and 2, but will always be with you to give you luck.', [1, 2])
    die2 = Die('Super', 'Boom', [1, 2])

    rageblade = StatItem('Rage Blade', 'Guinoos', 0, 0, 0)
    monster = StatItem('Monster', 'Monster', 0, 0, 0)

    # Make enemy
    enemy = EnemyCharacter('Baron', 50, 3, 3, 5, monster, 30, True)
    enemy.add_item(monster)
    enemy.add_item(die2)

    enemy.setAttack('spits venom')
    enemy.setFlee('blocks you with his tail')
    enemy.setDeath('wails in pain as it shrivels and dies')

    # Make player
    player = PlayerCharacter(20, 3, 10)
    player.add_item(rageblade)
    player.add_item(die1)

    # Fight!
    for i in range(0, 5):
        battle = Battle(player, enemy)
        battle.start_battle()

    if battle.won():
        print("Player won")

    elif battle.fleed():
        print("Fleed")

    elif battle.lost():
        print("Lost")
    