import random

class Hangman:
    def __init__(self, word_pool, num_lives=5):
        self.word_pool = word_pool
        self.target_word = random.choice(word_pool)
        self.word_display = ["_" for _ in self.target_word]
        self.remaining_unique_letters = len(set(self.target_word))
        self.lives_left = num_lives
        self.guessed_letters = []

    def validate_guess(self, guess):
        return len(guess) == 1 and guess.isalpha()

    def has_been_guessed(self, guess):
        return guess in self.guessed_letters

    def reveal_letter_positions(self, guess):
        for index, letter in enumerate(self.target_word):
            if letter == guess:
                self.word_display[index] = guess

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.target_word:
            print(f"Good guess! {guess} is in the word.")
            self.reveal_letter_positions(guess)
            self.remaining_unique_letters -= 1
        else:
            self.lives_left -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.lives_left} lives left.")

    def ask_for_input(self):
        while True:
            guess = input("Enter a single letter: ")
            if not self.validate_guess(guess):
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif self.has_been_guessed(guess):
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.guessed_letters.append(guess)
                break

game = Hangman(["apple", "banana", "cherry"])
game.ask_for_input()
print("Word progress:", game.word_display)
print("Lives left:", game.lives_left)
print("Letters remaining:", game.remaining_unique_letters)
