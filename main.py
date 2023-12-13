# Password Plus?

import random

PLAYER_SCORE = 0
puzzle = [["abraham lincoln", "President", "Lawyer", "Republican", "Log Cabin"],
          ["family guy", "Tv Show", "Cartoon", "Rhode Island", "Talking baby"]]


# function to select a random puzzle


def main():
    selected_puzzle = random.choice(puzzle)
    answer, first_clue, second_clue, third_clue, fourth_clue = selected_puzzle
    while True:
        print(first_clue)
        guessed_answer = input("What is your guess? ")
        if guessed_answer.lower() == answer:
            print("You have guessed the right answer!")
            break
        else:
            print(first_clue, " | ", second_clue)
            guessed_answer = input("What is your guess? ")
            if guessed_answer.lower() == answer:
                print("Yes, that is correct")
                break
            else:
                print(first_clue, " | ", second_clue, " | ", third_clue)
                guessed_answer = input("What is your guess? ")
                if guessed_answer.lower() == answer:
                    print("Yes, you got it!")
                    break
                else:
                    print(first_clue, " | ", second_clue, " | ", third_clue, " | ", fourth_clue)
                    guessed_answer = input("What is your last guess? ")
                    if guessed_answer.lower() == answer:
                        print("You finally got it!")
                        break
                    else:
                        print("Sorry you did not guess the correct answer")
                        break


main()

