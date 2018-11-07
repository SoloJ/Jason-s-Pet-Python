import random

class GameEngine():
    def __init__(self, game_diffuclty):
        self.difficulty = game_diffuclty

    def SequenceGen(self):
        self.sequence = []
        for x in range(0,6):
            self.sequence.append(random.randint(1, 6))

    def UserInput(self):
        self.user_input = input("What is your Guess?..")

