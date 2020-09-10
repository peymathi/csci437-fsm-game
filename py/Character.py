class Character:
    
    def __init__(self, health, armor, damage, level):
        
        self.__health = health
        self.__armor = armor
        self.__damage = damage
        self.__level = level
        self.__exp = 0
        self.__inventory = []

    def generate_attack(self):
        pass

    def receive_attack(self, attack):
        pass