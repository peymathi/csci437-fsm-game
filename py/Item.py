class Item:

    def __init__(self, name, description, bonus, rollable):

        self.__name = name
        self.__description = description
        self.__bonus = bonus
        self.__rollable = rollable

    def isRollable(self):
        return self.__rollable

    def hasBonusStats(self):
        return self.__bonus
        
    def getName(self):
        return self.__name

    def getDescription(self):
        return self.__description

