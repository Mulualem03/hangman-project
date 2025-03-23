import random

fruit_list = ["apple", "banana", "cherry", "mango", "grape"]
print(fruit_list)

selected_fruit = random.choice(fruit_list)
print("Randomly chosen word:", selected_fruit)

user_input = input("Enter a single letter: ")
print("You guessed:", user_input)

if len(user_input) == 1 and user_input.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")
