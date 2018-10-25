import random


class Roll_Dice():
    def __init__(self, number_of_sides):
        self.sides_of_dice = number_of_sides

    def roller(self):
        self.results = random.randint(1, self.sides_of_dice)






