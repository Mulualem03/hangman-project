# Hangman Game

## Description
A simple Python implementation of the classic Hangman game. The computer randomly selects a word, and the user tries to guess it one letter at a time.

## Installation
1. Clone this repository:

2. Navigate to the project folder:

3. Run the Python file:

## Usage
- Run the script in terminal
- Enter a letter when prompted
- See if it's in the word

## File Structure

## License
This project is for educational use only.

## Milestone 3: Guess Checking

In this milestone, the program now asks the user to guess a letter and checks whether that letter is in the randomly chosen word. Input validation is handled using a function that ensures the user enters a single alphabetical character. The guess checking is also handled in a separate function for better organisation.

### How to Run

## Milestone 4: Hangman Class with Game Logic

This milestone introduces object-oriented programming to structure the game using a class.

### What's Implemented

- A `Hangman` class with the following:
  - Word selection from a given word list
  - Input validation through the `ask_for_input()` method
  - Letter checking and word progress updates using `check_guess()`
  - Lives system with feedback for correct and incorrect guesses
  - Tracking previously guessed letters

### How to Run


## Milestone 5: Putting It All Together

This milestone brings all components of the Hangman game together and allows the full game to be played start to finish using object-oriented programming.

### Game Logic Flow

- The main function `play_game()` controls the game loop.
- It uses the `Hangman` class defined in Milestone 4 to:
  - Pick a random word
  - Ask the player to guess letters
  - Track correct guesses and lives
  - Detect if the player has won or lost

### How to Run the Game


### What I Learned

- How to break a problem into small, testable parts
- Using classes and methods to manage game state
- Input validation and clean loop control
- How to make the code user-friendly and readable
