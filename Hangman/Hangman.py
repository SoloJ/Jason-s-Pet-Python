import random
import letter_check


def word_select():
    word_list = open("/Users/jasonsolomon/PycharmProjects/Jason-s-Pet-Python/Hangman/words.txt")
    contents_of_file = word_list.read()
    word_list.close()
    words = contents_of_file.split()
    global chosen_word
    chosen_word = random.choice(words)


word_select()


def input_guess():
    guess = input("What is your Guess?..")
    answer = letter_check.LetterCheck(chosen_word, guess)
    answer.checker()
    print(answer.guess)
    print(answer.word)
    print(answer.correct)
input_guess()
exit()
