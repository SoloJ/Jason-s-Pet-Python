import random

def word_choser():
    word_list = open("/Users/jasonsolomon/PycharmProjects/Jason-s-Pet-Python/Hangman/Hangman.py")
    contents_of_file = word_list.read()
    word_list.close()
    words = contents_of_file.split()
    chosen_word = random.choice(words)

word_choser()

