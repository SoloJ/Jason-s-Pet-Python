import random

class GameEngine():
    def __init__(self, game_difficulty, color_decoder):
        self.difficulty = game_difficulty
        self.decoder = color_decoder

    def SequenceGen(self):
        self.sequence = []
        self.sequence_word = []
        for x in range(0, int(self.difficulty)):
            self.sequence.append(random.randint(1, int(self.difficulty)))
        for x in self.sequence:
            self.sequence_word.append(self.decoder[str(x)])


    def ColorKey(self):
        for x in self.decoder:
            print(x + " = " + self.decoder[str(x)])

    def UserInput(self):
        self.user_input = input("What is your Guess?..")

