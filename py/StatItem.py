from Item import Item

class StatItem (Item):

    def __init__(self, name, description, bonusArmor, bonusDamage, bonusHealth):
        super().__init__(name, description)
        self.__bonus_armor = bonusArmor
        self.__bonus_damage = bonusDamage
        self.__bonus_health = bonusHealth

    def health(self):
        return self.__bonus_health

    def armor(self):
        return self.__bonus_armor

    def damage(self):
        return self.__bonus_damage