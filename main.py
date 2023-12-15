# Password Plus?

import random

class Puzzle:
  def __init__(self, password, clues):
    self.password = password
    self.clues = clues

PLAYER_SCORE = 0
# 1) Created a Puzzle class (has a "password" property and string list of "clues") - Puzzle.py
# 2) Created a list of multiple puzzles
# 3) Made a new function called playPuzzle() that holds the logic for playing a password and handling guesses (Loop through all of the clues until the password is guessed OR we run out of clues)
# 4) Ask player how many passwords to play
# 5) Play all the passwords

puzzles = [
            Puzzle("abraham lincoln",["President", "Lawyer", "Republican", "Log Cabin"])
            , Puzzle("family guy",["Tv Show", "Cartoon", "Rhode Island", "Talking baby"])
            , Puzzle("golden girls",["Blanche", "Rose", "Dorothy", "Sophia"])
            ]


def playPuzzle(puzzle):
    answer = puzzle.password
    
    clues_so_far = ""
    guessed_correctly = False
    variable_wording = ["first", "second", "third", "final"]
    clue_number = 0

    # Loop through each clue
    for clue in puzzle.clues:

        # Concatenate the current clue with clues seen so far
        if clue_number > 0:
            clues_so_far = clue + " | " + clues_so_far
        else:
            clues_so_far = clue

        print(clues_so_far)

        guessed_answer = input("What is your " + variable_wording[clue_number] + " guess? ")
        if guessed_answer.lower() == answer:
            print("You have guessed the right answer!")
            guessed_correctly = True
            break
        else:
            print("That's not the password")
        
        clue_number = clue_number + 1

    # All clues have been presented OR the player guessed correctly
    if guessed_correctly == False:
        print("The correct password was: " + answer)

def main():
    print("It's more than Password...it's Password Plus!")

    passwords_to_play = input("How many passwords do you want to play? (1 to " + str(len(puzzles)) + ")")

    # Play
    for current_password_number in range(int(passwords_to_play)):
        print("===== Password #" + str(current_password_number + 1) + "=====")
        # function to select a random puzzle - TODO remove puzzles after playing them so it's truly random
        selected_puzzle = random.choice(puzzles)

        # Call the playPuzzle function which contains the logic for giving clues and checking guesses
        playPuzzle(selected_puzzle)
    
    print("====================")
    print("Thanks for playing!")
    

main()

