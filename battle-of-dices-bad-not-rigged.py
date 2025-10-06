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
stop = 6

# Round 1
input("\nPress ENTER to roll the dice...")

player1_round1_roll = random.randint(start, stop)

print("Player 1 rolled: ", player1_round1_roll)

player2_round1_roll = random.randint(start, stop)

print("Player 2 rolled: ", player2_round1_roll)

input("\nPress ENTER to continue...")

# So far so good right? But how to check who got the highest roll?

if player1_round1_roll > player2_round1_roll:
    player1_wins += 1
    print("Player 1 wins this round!")
    print("Because ", player1_round1_roll," is greater than ", player2_round1_roll)
elif player1_round1_roll == player2_round1_roll:
    print("Amaaazzinng! This round has a tie!")
else:
    player2_wins = player2_wins + 1
    print("Player 2 wins this round!")
    print("Because ", player2_round1_roll," is greater than ", player1_round1_roll)

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

player1_round2_roll = random.randint(start, stop)

print("Player 1 rolled: ", player1_round2_roll)

player2_round2_roll = random.randint(start, stop)

print("Player 2 rolled: ", player2_round2_roll)

input("\nPress ENTER to continue...")

# So far so good right? But how to check who got the highest roll?

if player1_round2_roll > player2_round2_roll:
    player1_wins += 1
    print("Player 1 wins this round!")
    print("Because ", player1_round2_roll," is greater than ", player2_round2_roll)
elif player1_round2_roll == player2_round2_roll:
    print("Amaaazzinng! This round has a tie!")
else:
    player2_wins = player2_wins + 1
    print("Player 2 wins this round!")
    print("Because ", player2_round2_roll," is greater than ", player1_round2_roll)
    
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

player1_round3_roll = random.randint(start, stop)

print("Player 1 rolled: ", player1_round3_roll)

player2_round3_roll = random.randint(start, stop)

print("Player 2 rolled: ", player2_round3_roll)

input("\nPress ENTER to continue...")

# So far so good right? But how to check who got the highest roll?

if player1_round3_roll > player2_round3_roll:
    player1_wins += 1
    print("Player 1 wins this round!")
    print("Because ", player1_round3_roll," is greater than ", player2_round3_roll)
elif player1_round3_roll == player2_round3_roll:
    print("Amaaazzinng! This round has a tie!")
else:
    player2_wins = player2_wins + 1
    print("Player 2 wins this round!")
    print("Because ", player2_round3_roll," is greater than ", player1_round3_roll)

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

player1_round4_roll = random.randint(start, stop)

print("Player 1 rolled: ", player1_round4_roll)

player2_round4_roll = random.randint(start, stop)

print("Player 2 rolled: ", player2_round4_roll)

input("\nPress ENTER to continue...")

# So far so good right? But how to check who got the highest roll?

if player1_round4_roll > player2_round4_roll:
    player1_wins += 1
    print("Player 1 wins this round!")
    print("Because ", player1_round4_roll," is greater than ", player2_round4_roll)
elif player1_round4_roll == player2_round4_roll:
    print("Amaaazzinng! This round has a tie!")
else:
    player2_wins = player2_wins + 1
    print("Player 2 wins this round!")
    print("Because ", player2_round4_roll," is greater than ", player1_round4_roll)

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

player1_round5_roll = random.randint(start, stop)

print("Player 1 rolled: ", player1_round5_roll)

player2_round5_roll = random.randint(start, stop)

print("Player 2 rolled: ", player2_round5_roll)

input("\nPress ENTER to continue...")

# So far so good right? But how to check who got the highest roll?

if player1_round5_roll > player2_round5_roll:
    player1_wins += 1
    print("Player 1 wins this round!")
    print("Because ", player1_round5_roll," is greater than ", player2_round5_roll)
elif player1_round5_roll == player2_round5_roll:
    print("Amaaazzinng! This round has a tie!")
else:
    player2_wins = player2_wins + 1
    print("Player 2 wins this round!")
    print("Because ", player2_round5_roll," is greater than ", player1_round5_roll)

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

player1_round6_roll = random.randint(start, stop)

print("Player 1 rolled: ", player1_round6_roll)

player2_round6_roll = random.randint(start, stop)

print("Player 2 rolled: ", player2_round6_roll)

input("\nPress ENTER to continue...")

# So far so good right? But how to check who got the highest roll?

if player1_round6_roll > player2_round6_roll:
    player1_wins += 1
    print("Player 1 wins this round!")
    print("Because ", player1_round6_roll," is greater than ", player2_round6_roll)
elif player1_round6_roll == player2_round6_roll:
    print("Amaaazzinng! This round has a tie!")
else:
    player2_wins = player2_wins + 1
    print("Player 2 wins this round!")
    print("Because ", player2_round6_roll," is greater than ", player1_round6_roll)

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

player1_round7_roll = random.randint(start, stop)

print("Player 1 rolled: ", player1_round7_roll)

player2_round7_roll = random.randint(start, stop)

print("Player 2 rolled: ", player2_round7_roll)

input("\nPress ENTER to continue...")

# So far so good right? But how to check who got the highest roll?

if player1_round7_roll > player2_round7_roll:
    player1_wins += 1
    print("Player 1 wins this round!")
    print("Because ", player1_round7_roll," is greater than ", player2_round7_roll)
elif player1_round7_roll == player2_round7_roll:
    print("Amaaazzinng! This round has a tie!")
else:
    player2_wins = player2_wins + 1
    print("Player 2 wins this round!")
    print("Because ", player2_round7_roll," is greater than ", player1_round7_roll)

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

player1_round8_roll = random.randint(start, stop)

print("Player 1 rolled: ", player1_round8_roll)

player2_round8_roll = random.randint(start, stop)

print("Player 2 rolled: ", player2_round8_roll)

input("\nPress ENTER to continue...")

# So far so good right? But how to check who got the highest roll?

if player1_round8_roll > player2_round8_roll:
    player1_wins += 1
    print("Player 1 wins this round!")
    print("Because ", player1_round8_roll," is greater than ", player2_round8_roll)
elif player1_round8_roll == player2_round8_roll:
    print("Amaaazzinng! This round has a tie!")
else:
    player2_wins = player2_wins + 1
    print("Player 2 wins this round!")
    print("Because ", player2_round8_roll," is greater than ", player1_round8_roll)

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

player1_round9_roll = random.randint(start, stop)

print("Player 1 rolled: ", player1_round9_roll)

player2_round9_roll = random.randint(start, stop)

print("Player 2 rolled: ", player2_round9_roll)

input("\nPress ENTER to continue...")

# So far so good right? But how to check who got the highest roll?

if player1_round9_roll > player2_round9_roll:
    player1_wins += 1
    print("Player 1 wins this round!")
    print("Because ", player1_round9_roll," is greater than ", player2_round9_roll)
elif player1_round9_roll == player2_round9_roll:
    print("Amaaazzinng! This round has a tie!")
else:
    player2_wins = player2_wins + 1
    print("Player 2 wins this round!")
    print("Because ", player2_round9_roll," is greater than ", player1_round9_roll)

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

player1_round10_roll = random.randint(start, stop)

print("Player 1 rolled: ", player1_round10_roll)

player2_round10_roll = random.randint(start, stop)

print("Player 2 rolled: ", player2_round10_roll)

input("\nPress ENTER to continue...")

# So far so good right? But how to check who got the highest roll?

if player1_round10_roll > player2_round10_roll:
    player1_wins += 1
    print("Player 1 wins this round!")
    print("Because ", player1_round10_roll," is greater than ", player2_round10_roll)
elif player1_round10_roll == player2_round10_roll:
    print("Amaaazzinng! This round has a tie!")
else:
    player2_wins = player2_wins + 1
    print("Player 2 wins this round!")
    print("Because ", player2_round10_roll," is greater than ", player1_round10_roll)

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

player1_round11_roll = random.randint(start, stop)

print("Player 1 rolled: ", player1_round11_roll)

player2_round11_roll = random.randint(start, stop)

print("Player 2 rolled: ", player2_round11_roll)

input("\nPress ENTER to continue...")

# So far so good right? But how to check who got the highest roll?

if player1_round11_roll > player2_round11_roll:
    player1_wins += 1
    print("Player 1 wins this round!")
    print("Because ", player1_round11_roll," is greater than ", player2_round11_roll)
elif player1_round11_roll == player2_round11_roll:
    print("Amaaazzinng! This round has a tie!")
else:
    player2_wins = player2_wins + 1
    print("Player 2 wins this round!")
    print("Because ", player2_round11_roll," is greater than ", player1_round11_roll)

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

player1_round12_roll = random.randint(start, stop)

print("Player 1 rolled: ", player1_round12_roll)

player2_round12_roll = random.randint(start, stop)

print("Player 2 rolled: ", player2_round12_roll)

input("\nPress ENTER to continue...")

# So far so good right? But how to check who got the highest roll?

if player1_round12_roll > player2_round12_roll:
    player1_wins += 1
    print("Player 1 wins this round!")
    print("Because ", player1_round12_roll," is greater than ", player2_round12_roll)
elif player1_round12_roll == player2_round12_roll:
    print("Amaaazzinng! This round has a tie!")
else:
    player2_wins = player2_wins + 1
    print("Player 2 wins this round!")
    print("Because ", player2_round12_roll," is greater than ", player1_round12_roll)

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

player1_round13_roll = random.randint(start, stop)

print("Player 1 rolled: ", player1_round13_roll)

player2_round13_roll = random.randint(start, stop)

print("Player 2 rolled: ", player2_round13_roll)

input("\nPress ENTER to continue...")

# So far so good right? But how to check who got the highest roll?

if player1_round13_roll > player2_round13_roll:
    player1_wins += 1
    print("Player 1 wins this round!")
    print("Because ", player1_round13_roll," is greater than ", player2_round13_roll)
elif player1_round13_roll == player2_round13_roll:
    print("Amaaazzinng! This round has a tie!")
else:
    player2_wins = player2_wins + 1
    print("Player 2 wins this round!")
    print("Because ", player2_round13_roll," is greater than ", player1_round13_roll)

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

player1_round14_roll = random.randint(start, stop)

print("Player 1 rolled: ", player1_round14_roll)

player2_round14_roll = random.randint(start, stop)

print("Player 2 rolled: ", player2_round14_roll)

input("\nPress ENTER to continue...")

# So far so good right? But how to check who got the highest roll?

if player1_round14_roll > player2_round14_roll:
    player1_wins += 1
    print("Player 1 wins this round!")
    print("Because ", player1_round14_roll," is greater than ", player2_round14_roll)
elif player1_round14_roll == player2_round14_roll:
    print("Amaaazzinng! This round has a tie!")
else:
    player2_wins = player2_wins + 1
    print("Player 2 wins this round!")
    print("Because ", player2_round14_roll," is greater than ", player1_round14_roll)

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

player1_round15_roll = random.randint(start, stop)

print("Player 1 rolled: ", player1_round15_roll)

player2_round15_roll = random.randint(start, stop)

print("Player 2 rolled: ", player2_round15_roll)

input("\nPress ENTER to continue...")

# So far so good right? But how to check who got the highest roll?

if player1_round15_roll > player2_round15_roll:
    player1_wins += 1
    print("Player 1 wins this round!")
    print("Because ", player1_round15_roll," is greater than ", player2_round15_roll)
elif player1_round15_roll == player2_round15_roll:
    print("Amaaazzinng! This round has a tie!")
else:
    player2_wins = player2_wins + 1
    print("Player 2 wins this round!")
    print("Because ", player2_round15_roll," is greater than ", player1_round15_roll)

# We can print the game score:
print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

# Now we need to check if either player won.
if player1_wins == 3:
    print("Player 1 is the newest Battle of Dices Lifetime Championship Winner! ")
elif player2_wins == 3:
    print("Player 2 is the newest Battle of Dices Lifetime Championship Winner! ")
else:
    print("This heated Battle of Dices is still going on! Who will win in the end? Stay Tuned! ")

# Round 16
input("\nPress ENTER to roll the dice...")

player1_round16_roll = random.randint(start, stop)

print("Player 1 rolled: ", player1_round16_roll)

player2_round16_roll = random.randint(start, stop)

print("Player 2 rolled: ", player2_round16_roll)

input("\nPress ENTER to continue...")

# So far so good right? But how to check who got the highest roll?

if player1_round16_roll > player2_round16_roll:
    player1_wins += 1
    print("Player 1 wins this round!")
    print("Because ", player1_round16_roll," is greater than ", player2_round16_roll)
elif player1_round16_roll == player2_round16_roll:
    print("Amaaazzinng! This round has a tie!")
else:
    player2_wins = player2_wins + 1
    print("Player 2 wins this round!")
    print("Because ", player2_round16_roll," is greater than ", player1_round16_roll)

# We can print the game score:
print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

# Now we need to check if either player won.
if player1_wins == 3:
    print("Player 1 is the newest Battle of Dices Lifetime Championship Winner! ")
elif player2_wins == 3:
    print("Player 2 is the newest Battle of Dices Lifetime Championship Winner! ")

print ("The exact numbers of the rounds:")
print ("Player 1 -",player1_round1_roll,"|",player1_round2_roll,"|", player1_round3_roll,"|", player1_round4_roll,"|", player1_round5_roll,"|", player1_round6_roll,"|", player1_round7_roll,"|", player1_round8_roll,"|", player1_round9_roll,"|", player1_round10_roll,"|", player1_round11_roll,"|", player1_round12_roll,"|", player1_round13_roll, "|",player1_round14_roll,"|", player1_round15_roll,"|", player1_round16_roll)
print ("Player 2 -",player2_round1_roll,"|",player2_round2_roll,"|", player2_round3_roll,"|", player2_round4_roll,"|", player2_round5_roll,"|", player2_round6_roll,"|", player2_round7_roll,"|", player2_round8_roll,"|", player2_round9_roll,"|", player2_round10_roll,"|", player2_round11_roll,"|", player2_round12_roll,"|", player2_round13_roll, "|",player2_round14_roll,"|", player2_round15_roll,"|", player2_round16_roll)