import random
import letter_check


def word_select():
    word_list = open("/Users/jasonsolomon/PycharmProjects/Jason-s-Pet-Python/Hangman/words.txt")
    contents_of_file = word_list.read()
    word_list.close()
    words = contents_of_file.split()
    global chosen_word
    global chosen_word_length
    global blank_display_word
    blank_display_word = list()
    chosen_word = random.choice(words)
    chosen_word_length = len(chosen_word)
    n = 0

    while n < chosen_word_length:
        blank_display_word.insert(n, "-")
        n=n+1

word_select()


def input_guess():
    guess = input("What is your Guess?..")
    answer = letter_check.LetterCheck(chosen_word, guess)
    answer.checker()
    global display_word
    display_word = list(chosen_word)
    print(chosen_word)
    print(answer.correct)
    print(answer.guess)
    found_letter = "false"


    if answer.correct == "true":
        n = 0
        while found_letter == "false":
            if answer.guess not in chosen_word[n]:
                n = n + 1
            else:
                found_letter == "true"
                word_guess_position = n
                break
    elif answer.correct == "false":
        input_guess()

    blank_display_word.pop(n)
    blank_display_word.insert(n, display_word[n])
    input_guess()


    if "-" not in blank_display_word:
        print("you did it")
        exit()

input_guess()













exit()
