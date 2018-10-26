
class LetterCheck():
    def __init__(self, chosen_word, guessed_letter):
        self.word = chosen_word
        self.guess = guessed_letter

    def checker(self):
        if self.guess in self.word:
            self.correct = "true"

        else:
            self.correct = "false"
