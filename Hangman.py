#Create random word
import random
from Hangman_Words import words 
from Hangman_Art import logo, stages
print(logo)
end_game = False
rand_word = random.choice(words)
lives = 6
print(f"You have {lives} lives to guess the word.")
# create board
word_length = len(rand_word)
board = []
guessed_letters = []
for char in range(word_length):
    board += ["_"]
print(f"Your chosen word is: \n{board}")

# for each letter in random word generate a blank space
while not end_game:
    # ask user to guess a letter
    guess = input("Please guess a letter \n").lower()
    # show used letters
    # join all elements in the list [guessed_letters] and turn it into a string.
    guessed_letters += guess
    print(f"letters used: {' '.join(guessed_letters)}")
    # add guess to board if correct
    for position in range(word_length):
        letter = rand_word[position]
        if guess == letter:
            board[position] = letter
    # join all elements in the list [board] and turn it into a string.
    print(f"{' '.join(board)}")
    if guess not in rand_word:
        lives -= 1
        art = stages[lives]
        print(art)
        print(f"Incorrect. You have {lives} lives left.")
    else:
        print(f"Correct.")  

    if "_" not in board:
        print("You win!")
        end_game = True
        
    if lives == 0:
        print(f"The word was {rand_word}. Better luck next time.")
        end_game = True
    


    
