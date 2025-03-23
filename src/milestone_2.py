import random

word_list = ["apple", "banana", "cherry", "mango", "grape"]
print(word_list)

word = random.choice(word_list)
print("Randomly chosen word:", word)

guess = input("Enter a single letter: ")
print("You guessed:", guess)

if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")
