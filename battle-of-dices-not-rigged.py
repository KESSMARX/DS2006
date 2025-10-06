# Battle of Dices is going to be an amazing 2 player game, 
# where two players face each other using only their sheer luck! 
# 
# The rules are:
# 
# Each player throws one D6.
# The player with the highest roll wins the round.  
# The first player to win 3 times is the winner.
#
# Our main task today is to implement the code necessary to bring this
# amazing game alive!

import random
import BOD_functions

print("🎲 Welcome to Battle of Dices! 🎲")

# Variables to keep track of the score:
player1_wins = 0
player2_wins = 0
total_rounds = 0
player1_score_list = []
player2_score_list = []

# ----------------------------------------------------------------------------------

while player1_wins < 3 and player2_wins < 3 :

    # Round 1

    total_rounds += 1

    input("\nPress ENTER to roll the dice...")  
    player1_roll = BOD_functions.rollD20()
    player1_score_list.append(player1_roll)
    print("Player 1 rolled: ", player1_roll)

    player2_roll = BOD_functions.rollD20()
    player2_score_list.append(player2_roll)
    print("Player 2 rolled: ", player2_roll)

    input("\nPress ENTER to continue...")

    # So far so good right? But how to check who got the highest roll?

    if player1_roll > player2_roll:
        player1_wins += 1
        print("Player 1 wins round", total_rounds, "!")
        print("Because ", player1_roll," is greater than ", player2_roll)
    elif player1_roll == player2_roll:
        print("Amaaazzinng! This round has a tie!")
    else:
        player2_wins = player2_wins + 1
        print("Player 2 wins round", total_rounds, "!")
        print("Because ", player2_roll," is greater than ", player1_roll)

    # We can print the game score:
    print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

    # Now we need to check if either player won.
    if player1_wins == 3:
        print("Player 1 is the newest Battle of Dices Lifetime Championship Winner! ")
    elif player2_wins == 3:
        print("Player 2 is the newest Battle of Dices Lifetime Championship Winner! ")
    else:
        print("This heated Battle of Dices is still going on! Who will win in the end? Stay Tuned! ")

# Summarize of all the rounds

print("This game has been played in", total_rounds, "rounds with a dice of 20 sites.")
print("Player 1", player1_score_list)
print("Player 2", player2_score_list)

# Safe the results

filename = input("Please enter the filename to save the results:")

with open(filename, "w") as file: # "w" = write mode
    file.write (f"Player 1 rolled {player1_score_list} \nPlayer 2 rolled {player2_score_list}\n")


