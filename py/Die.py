from Item import Item
import random

class Die (Item):

    def __init__(self, name, description, values):
        super().__init__(name, description)
        self.__values = values

    def roll(self):
        return random.choice(self.__values)

# Testing
if __name__ == '__main__':
    test = Die("test", "test", [2, 3, 5, 6, 8])
    print(test.roll())