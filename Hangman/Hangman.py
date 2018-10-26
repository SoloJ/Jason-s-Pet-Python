import random
import letter_check


def word_select():
    word_list = open("/Users/jasonsolomon/PycharmProjects/Jason-s-Pet-Python/Hangman/words.txt")
    contents_of_file = word_list.read()
    word_list.close()
    words = contents_of_file.split()
    global chosen_word
    global chosen_word_length
    chosen_word = random.choice(words)
    chosen_word_length = len(chosen_word)

word_select()


def input_guess():
    guess = input("What is your Guess?..")
    answer = letter_check.LetterCheck(chosen_word, guess)
    answer.checker()
    print(chosen_word)
    print(answer.correct)
    print(answer.guess)

input_guess()








exit()
