# Password Plus?
# Super Password?

import os
import random
import json
from types import SimpleNamespace


class Puzzle:
  def __init__(self, password, clues):
    self.password = password
    self.clues = clues


class Player:
    def __init__(self, name, score):
        self.score = score
        self.name = name


# 1) Created a Puzzle class (has a "password" property and string list of "clues") - Puzzle.py
# 2) Created a list of multiple puzzles
# 3) Made a new function called playPuzzle() that holds the logic for playing a password and handling guesses (Loop through all of the clues until the password is guessed OR we run out of clues)
# 4) Ask player how many passwords to play
# 5) Play all the passwords

puzzles = [
            Puzzle("abraham lincoln",["President", "Lawyer", "Republican", "Log Cabin"])
            , Puzzle("family guy",["Tv Show", "Cartoon", "Rhode Island", "Talking baby"])
            , Puzzle("golden girls",["Blanche", "Rose", "Dorothy", "Sophia"])
            , Puzzle("butter",["churn", "milk", "cream", "yellow"])
            , Puzzle("grape",["bunch", "purple", "wine", "fruit"])
            , Puzzle("toaster",["bread", "pop", "brown", "cooked"])
            ]

# Create an instance of the Player class (it will be accessible globally)
current_player = Player("no name", 0)
player_data_from_file = []

def playPuzzle(puzzle):
    answer = puzzle.password
    
    clues_so_far = ""
    guessed_correctly = False
    variable_wording = ["first", "second", "third", "final"]
    clue_number = 0
    point_values = [100, 75, 50, 25]

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
            print(f"You have guessed the right answer! You earned {point_values[clue_number]} points.")
            guessed_correctly = True
            current_player.score += point_values[clue_number]
            break
        else:
            print("That's not the password")
        
        clue_number = clue_number + 1

    # All clues have been presented OR the player guessed correctly
    if guessed_correctly == False:
        print("The correct password was: " + answer)


def high_scores():
    with open("Log", "r") as f:
        score = f.read()
        print(score)


def to_json(obj):
    return json.dumps(obj, default=lambda obj: obj.__dict__)

def save_data(player_to_save, file_path):
    remove_previously_saved_data(player_to_save, file_path)
    append_save_data(player_to_save, file_path)
    pass

def append_save_data(player_to_save, file_path):
    data_as_json = to_json(player_to_save)

    with open(file_path, 'a') as out:
        out.write(data_as_json + '\n')
    
    print("Data saved to file: " + file_path)

def clear_file_data(file_path):
    with open(file_path, 'w'):
        pass

def get_all_player_data(log_path):
    data_from_file = []
            
    with open(log_path, 'r', encoding='UTF-8') as f:
        while line := f.readline():
            if line != '':
                line_as_json = json.loads(line, object_hook=lambda d: SimpleNamespace(**d))
                data_from_file.append(line_as_json)

    return data_from_file

def remove_previously_saved_data(player_name, log_path):
    all_players = get_all_player_data(log_path)

    # Find the first record with a matching player name
    line_to_delete = -1
    for number, p in enumerate(all_players):
        if p.name == player_name.name:
            line_to_delete = number

    # Remove the player's data, clear the file, and resave the file with players re-added
    if line_to_delete > -1:
        all_players.pop(line_to_delete)

        clear_file_data(log_path)

        for p in all_players:
            append_save_data(p, log_path)


def select_player_from_file(player_list):
    x = 1
    print("===== Players =====")
    for p in player_list:
        print(f'{x}. {p.name} - {p.score}')
        x = x + 1 
    
    x = x - 1

    valid_choice = False
    selected_player_index = 0
    while valid_choice == False:
        selected_player_text = input(f"Choose a player (1 to {x}): ")

        if selected_player_text.isdigit():
            selected_player_index = int(selected_player_text)

            if selected_player_index <= 0 or selected_player_index > x:
                valid_choice = False
            else:
                valid_choice = True
    
    return player_list[selected_player_index - 1]


def display_high_scores_from_file(player_list):
    x = 1

    # Sort the list by Score
    sorted_list = sorted(player_list, key=lambda x: x.score, reverse=True)

    print("===== High Scores =====")
    for p in sorted_list:
        print(f'{x}. {p.name} - {p.score}')
        x = x + 1 

def main():
     # Change the working directory to the place where this .py file is located so that relative paths will work
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    # Create a directory for storing logs/files and set the path for the scores
    logs_directory = "logs"
    if not os.path.exists(logs_directory):
        os.makedirs(logs_directory)
    scores_log_path = os.path.join(logs_directory, 'scores.log')

    # Tell Python to use the Global current_player variable
    global current_player

    print("It's more than Password...it's Password Plus!")

    # Asking if the player would want to play or see the High Scores
    display_menu = True
    start_game = 0
    while display_menu:
        
        start_game = input("Select an Option:\r\n1) Play Password Plus\r\n2) View high scores\r\n3) Load saved player data\r\n4) Quit\r\n")
        if start_game == "1":
            display_menu = False
            break
        elif start_game == "2":
            player_data_from_file = get_all_player_data(scores_log_path)

            if len(player_data_from_file) > 0:
                display_high_scores_from_file(player_data_from_file)
            else:
                print("No previous save data found")
            
            #high_scores()
        elif start_game == "3":
            player_data_from_file = get_all_player_data(scores_log_path)

            if len(player_data_from_file) > 0:
                current_player = select_player_from_file(player_data_from_file)
            else:
                print("No previous save data found")
        elif start_game == "4":
            display_menu = False
            break
        else:
            print("Please select a valid option.")

    if start_game == "1":
        # If a player's data was not loaded from file, ask for their name
        if current_player.name != "no name":
            print(f"Player loaded from file: {current_player.name}")
        else:
            current_player.name = input("What is your Player Name? ")


        passwords_to_play = input("How many passwords do you want to play? (1 to " + str(len(puzzles)) + ") ")

        # Play
        for current_password_number in range(int(passwords_to_play)):
            print("===== Password #" + str(current_password_number + 1) + "=====")
            selected_puzzle = random.choice(puzzles)
            puzzles.remove(selected_puzzle)

            # Call the playPuzzle function which contains the logic for giving clues and checking guesses
            playPuzzle(selected_puzzle)
        
        print("====================")

        save_data(current_player, scores_log_path)

        print("Thanks for playing", current_player.name + "!")
        print("Your score was", current_player.score)

        # Created a log to store username and player scores
        #log_information = current_player.name, current_player.score
        #file = open('Log', 'a')
        #file.write(str(log_information))
        #file.close()
    else:
        print("See ya!")


main()

