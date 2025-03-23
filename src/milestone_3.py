import random

def get_single_letter():
    while True:
        input_letter = input("Enter a single letter: ")
        if len(input_letter) == 1 and input_letter.isalpha():
            return input_letter
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

def is_letter_in_word(letter, word):
    if letter in word:
        print("Good guess! The letter is in the word.")
    else:
        print("Sorry, the letter is not in the word.")

def run_hangman_turn(word_pool):
    chosen_word = random.choice(word_pool)
    player_guess = get_single_letter()
    is_letter_in_word(player_guess, chosen_word)

word_bank = ["apple", "banana", "cherry", "mango", "grape"]
run_hangman_turn(word_bank)
