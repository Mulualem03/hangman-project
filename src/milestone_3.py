import random

def get_valid_input():
    while True:
        user_input = input("Enter a single letter: ")
        if len(user_input) == 1 and user_input.isalpha():
            return user_input
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

def check_guess(letter, word):
    if letter in word:
        print("Good guess! The letter is in the word.")
    else:
        print("Sorry, the letter is not in the word.")

word_list = ["apple", "banana", "cherry", "mango", "grape"]
selected_word = random.choice(word_list)

guess = get_valid_input()
check_guess(guess, selected_word)
