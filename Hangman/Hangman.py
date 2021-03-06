import random
import letter_check


def word_select():
    word_list = open("/Users/jasonsolomon/PycharmProjects/Jason-s-Pet-Python/Hangman/words.txt")
    contents_of_file = word_list.read()
    word_list.close()
    words = contents_of_file.split()
    chosen_word = random.choice(words)
    answer = letter_check.LetterCheck(chosen_word)
    answer.blanker()
    answer.hangman_text()
    print(chosen_word)

    while "-" in answer.blank_display_word:
        print(answer.hangman_filled)
        answer.UserInput()
        answer.blank_filler()
        answer.hangman_text()

    print(chosen_word)
    print("You Win!!")

word_select()

