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

print("🎲 Welcome to Battle of Dices! 🎲")

# Variables to keep track of the score:
player1_wins = 0
player2_wins = 0

# Variables to edit the dice:
start = 1
stop = 20

# Round 1
input("\nPress ENTER to roll the dice...")

player1_roll = random.randint(start, stop)

print("Player 1 rolled: ", player1_roll)

player2_roll = random.randint(start, stop)

print("Player 2 rolled: ", player2_roll)

input("\nPress ENTER to continue...")

# So far so good right? But how to check who got the highest roll?

if player1_roll > player2_roll:
    player1_wins += 1
    print("Player 1 wins this round!")
    print("Because ", player1_roll," is greater than ", player2_roll)
elif player1_roll == player2_roll:
    print("Amaaazzinng! This round has a tie!")
else:
    player2_wins = player2_wins + 1
    print("Player 2 wins this round!")
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

# Since none of them would have won after 1 round, we could copy this code several times
# until we have enough times to make sure someone wins.

# Round 2
input("\nPress ENTER to roll the dice...")

player1_roll = random.randint(start, stop)

print("Player 1 rolled: ", player1_roll)

player2_roll = random.randint(start, stop)

print("Player 2 rolled: ", player2_roll)

input("\nPress ENTER to continue...")

# So far so good right? But how to check who got the highest roll?

if player1_roll > player2_roll:
    player1_wins += 1
    print("Player 1 wins this round!")
    print("Because ", player1_roll," is greater than ", player2_roll)
elif player1_roll == player2_roll:
    print("Amaaazzinng! This round has a tie!")
else:
    player2_wins = player2_wins + 1
    print("Player 2 wins this round!")
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

# Round 3
input("\nPress ENTER to roll the dice...")

player1_roll = random.randint(start, stop)

print("Player 1 rolled: ", player1_roll)

player2_roll = random.randint(start, stop)

print("Player 2 rolled: ", player2_roll)

input("\nPress ENTER to continue...")

# So far so good right? But how to check who got the highest roll?

if player1_roll > player2_roll:
    player1_wins += 1
    print("Player 1 wins this round!")
    print("Because ", player1_roll," is greater than ", player2_roll)
elif player1_roll == player2_roll:
    print("Amaaazzinng! This round has a tie!")
else:
    player2_wins = player2_wins + 1
    print("Player 2 wins this round!")
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

# Round 4
input("\nPress ENTER to roll the dice...")

player1_roll = random.randint(start, stop)

print("Player 1 rolled: ", player1_roll)

player2_roll = random.randint(start, stop)

print("Player 2 rolled: ", player2_roll)

input("\nPress ENTER to continue...")

# So far so good right? But how to check who got the highest roll?

if player1_roll > player2_roll:
    player1_wins += 1
    print("Player 1 wins this round!")
    print("Because ", player1_roll," is greater than ", player2_roll)
elif player1_roll == player2_roll:
    print("Amaaazzinng! This round has a tie!")
else:
    player2_wins = player2_wins + 1
    print("Player 2 wins this round!")
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

# Round 4
input("\nPress ENTER to roll the dice...")

player1_roll = random.randint(start, stop)

print("Player 1 rolled: ", player1_roll)

player2_roll = random.randint(start, stop)

print("Player 2 rolled: ", player2_roll)

input("\nPress ENTER to continue...")

# So far so good right? But how to check who got the highest roll?

if player1_roll > player2_roll:
    player1_wins += 1
    print("Player 1 wins this round!")
    print("Because ", player1_roll," is greater than ", player2_roll)
elif player1_roll == player2_roll:
    print("Amaaazzinng! This round has a tie!")
else:
    player2_wins = player2_wins + 1
    print("Player 2 wins this round!")
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

# Round 5
input("\nPress ENTER to roll the dice...")

player1_roll = random.randint(start, stop)

print("Player 1 rolled: ", player1_roll)

player2_roll = random.randint(start, stop)

print("Player 2 rolled: ", player2_roll)

input("\nPress ENTER to continue...")

# So far so good right? But how to check who got the highest roll?

if player1_roll > player2_roll:
    player1_wins += 1
    print("Player 1 wins this round!")
    print("Because ", player1_roll," is greater than ", player2_roll)
elif player1_roll == player2_roll:
    print("Amaaazzinng! This round has a tie!")
else:
    player2_wins = player2_wins + 1
    print("Player 2 wins this round!")
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

# Round 6
input("\nPress ENTER to roll the dice...")

player1_roll = random.randint(start, stop)

print("Player 1 rolled: ", player1_roll)

player2_roll = random.randint(start, stop)

print("Player 2 rolled: ", player2_roll)

input("\nPress ENTER to continue...")

# So far so good right? But how to check who got the highest roll?

if player1_roll > player2_roll:
    player1_wins += 1
    print("Player 1 wins this round!")
    print("Because ", player1_roll," is greater than ", player2_roll)
elif player1_roll == player2_roll:
    print("Amaaazzinng! This round has a tie!")
else:
    player2_wins = player2_wins + 1
    print("Player 2 wins this round!")
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

# Round 7
input("\nPress ENTER to roll the dice...")

player1_roll = random.randint(start, stop)

print("Player 1 rolled: ", player1_roll)

player2_roll = random.randint(start, stop)

print("Player 2 rolled: ", player2_roll)

input("\nPress ENTER to continue...")

# So far so good right? But how to check who got the highest roll?

if player1_roll > player2_roll:
    player1_wins += 1
    print("Player 1 wins this round!")
    print("Because ", player1_roll," is greater than ", player2_roll)
elif player1_roll == player2_roll:
    print("Amaaazzinng! This round has a tie!")
else:
    player2_wins = player2_wins + 1
    print("Player 2 wins this round!")
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

# Round 8
input("\nPress ENTER to roll the dice...")

player1_roll = random.randint(start, stop)

print("Player 1 rolled: ", player1_roll)

player2_roll = random.randint(start, stop)

print("Player 2 rolled: ", player2_roll)

input("\nPress ENTER to continue...")

# So far so good right? But how to check who got the highest roll?

if player1_roll > player2_roll:
    player1_wins += 1
    print("Player 1 wins this round!")
    print("Because ", player1_roll," is greater than ", player2_roll)
elif player1_roll == player2_roll:
    print("Amaaazzinng! This round has a tie!")
else:
    player2_wins = player2_wins + 1
    print("Player 2 wins this round!")
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

# Round 9
input("\nPress ENTER to roll the dice...")

player1_roll = random.randint(start, stop)

print("Player 1 rolled: ", player1_roll)

player2_roll = random.randint(start, stop)

print("Player 2 rolled: ", player2_roll)

input("\nPress ENTER to continue...")

# So far so good right? But how to check who got the highest roll?

if player1_roll > player2_roll:
    player1_wins += 1
    print("Player 1 wins this round!")
    print("Because ", player1_roll," is greater than ", player2_roll)
elif player1_roll == player2_roll:
    print("Amaaazzinng! This round has a tie!")
else:
    player2_wins = player2_wins + 1
    print("Player 2 wins this round!")
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

# Round 10
input("\nPress ENTER to roll the dice...")

player1_roll = random.randint(start, stop)

print("Player 1 rolled: ", player1_roll)

player2_roll = random.randint(start, stop)

print("Player 2 rolled: ", player2_roll)

input("\nPress ENTER to continue...")

# So far so good right? But how to check who got the highest roll?

if player1_roll > player2_roll:
    player1_wins += 1
    print("Player 1 wins this round!")
    print("Because ", player1_roll," is greater than ", player2_roll)
elif player1_roll == player2_roll:
    print("Amaaazzinng! This round has a tie!")
else:
    player2_wins = player2_wins + 1
    print("Player 2 wins this round!")
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

# Round 11
input("\nPress ENTER to roll the dice...")

player1_roll = random.randint(start, stop)

print("Player 1 rolled: ", player1_roll)

player2_roll = random.randint(start, stop)

print("Player 2 rolled: ", player2_roll)

input("\nPress ENTER to continue...")

# So far so good right? But how to check who got the highest roll?

if player1_roll > player2_roll:
    player1_wins += 1
    print("Player 1 wins this round!")
    print("Because ", player1_roll," is greater than ", player2_roll)
elif player1_roll == player2_roll:
    print("Amaaazzinng! This round has a tie!")
else:
    player2_wins = player2_wins + 1
    print("Player 2 wins this round!")
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

# Round 12
input("\nPress ENTER to roll the dice...")

player1_roll = random.randint(start, stop)

print("Player 1 rolled: ", player1_roll)

player2_roll = random.randint(start, stop)

print("Player 2 rolled: ", player2_roll)

input("\nPress ENTER to continue...")

# So far so good right? But how to check who got the highest roll?

if player1_roll > player2_roll:
    player1_wins += 1
    print("Player 1 wins this round!")
    print("Because ", player1_roll," is greater than ", player2_roll)
elif player1_roll == player2_roll:
    print("Amaaazzinng! This round has a tie!")
else:
    player2_wins = player2_wins + 1
    print("Player 2 wins this round!")
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

# Round 13
input("\nPress ENTER to roll the dice...")

player1_roll = random.randint(start, stop)

print("Player 1 rolled: ", player1_roll)

player2_roll = random.randint(start, stop)

print("Player 2 rolled: ", player2_roll)

input("\nPress ENTER to continue...")

# So far so good right? But how to check who got the highest roll?

if player1_roll > player2_roll:
    player1_wins += 1
    print("Player 1 wins this round!")
    print("Because ", player1_roll," is greater than ", player2_roll)
elif player1_roll == player2_roll:
    print("Amaaazzinng! This round has a tie!")
else:
    player2_wins = player2_wins + 1
    print("Player 2 wins this round!")
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

# Round 14
input("\nPress ENTER to roll the dice...")

player1_roll = random.randint(start, stop)

print("Player 1 rolled: ", player1_roll)

player2_roll = random.randint(start, stop)

print("Player 2 rolled: ", player2_roll)

input("\nPress ENTER to continue...")

# So far so good right? But how to check who got the highest roll?

if player1_roll > player2_roll:
    player1_wins += 1
    print("Player 1 wins this round!")
    print("Because ", player1_roll," is greater than ", player2_roll)
elif player1_roll == player2_roll:
    print("Amaaazzinng! This round has a tie!")
else:
    player2_wins = player2_wins + 1
    print("Player 2 wins this round!")
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

# Round 15
input("\nPress ENTER to roll the dice...")

player1_roll = random.randint(start, stop)

print("Player 1 rolled: ", player1_roll)

player2_roll = random.randint(start, stop)

print("Player 2 rolled: ", player2_roll)

input("\nPress ENTER to continue...")

# So far so good right? But how to check who got the highest roll?

if player1_roll > player2_roll:
    player1_wins += 1
    print("Player 1 wins this round!")
    print("Because ", player1_roll," is greater than ", player2_roll)
elif player1_roll == player2_roll:
    print("Amaaazzinng! This round has a tie!")
else:
    player2_wins = player2_wins + 1
    print("Player 2 wins this round!")
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

