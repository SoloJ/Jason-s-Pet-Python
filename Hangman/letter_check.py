
class LetterCheck():
    def __init__(self, chosen_word):
        self.word = chosen_word
        self.blank_display_word = list()
        self.chosen_word_length = len(chosen_word)
        self.guess = input("What is your Guess?..")
        self.display_word = list(chosen_word)


    def UserInput(self):  # requests another guess from the user
        self.guess = input("What is your Guess?..")

    def blanker(self):  # call once to create a blank array of length equal to the selected word

        n = 0
        while n < self.chosen_word_length:
            self.blank_display_word.insert(n, "-")
            n = n + 1

    def blank_filler(self): # call to fill in the blanked array with the guessed letter

        self.found_letter = "false"

        if self.guess in self.word:
            self.correct = "true"
        else:
            self.correct = "false"


        if self.correct == "true":
            n = 0
            while n < self.chosen_word_length:
                if self.guess in self.word[n]:
                    self.blank_display_word.pop(n)
                    self.blank_display_word.insert(n, self.display_word[n])
                    n = n + 1
                else:
                    n = n + 1


