from milestone_4 import Hangman

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    
    while True:
        if game.lives_left == 0:
            print("You lost!")
            break
        elif game.remaining_unique_letters > 0:
            game.ask_for_input()
        else:
            print("Congratulations. You won the game!")
            break

play_game(["apple", "banana", "cherry"])
