class Item:

    def __init__(self, name, description):
        
        self.__name = name
        self.__description = description
        
    def getName(self):
        return self.__name

    def getDescription(self):
        return self.__description

