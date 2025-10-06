import functions

# Number of rounds and gameover
rounds = 0
gameover = False

# Number of wins needed to win the game
winning_score = 3
2
# Array for storing the names of the players
player_names = []

# Array for storing the number of wins for each player
player_wins = []

# Obtain the number of players
number_of_players = int(input("How many players?"))

# For loop to obtain the player names
for i in range(number_of_players):
    name = input(f"What is the name of player {i+1}?")
    player_names.append(name)

# Initalize scores and rolls
for i in range(number_of_players):
    player_wins.append(0)

# Initalize player rolls as emtpy lists for each player 
player_rolls_history = [] # This will be a nested list

for i in range(number_of_players):
    # Add an emtpy list for each player
    player_rolls_history.append([])

# Repeats until the game is over. As many rounds as necessary 
while gameover is False:
    print(f"Round {rounds+1}")

    # Dice roll for each player in the current round
    current_rolls = []

    # We need to roll the dice for each player 
    for i in range(number_of_players):
        roll = functions.rollD6()
        current_rolls.append(roll)
        player_rolls_history[i].append(roll)
        print(f"Player{player_names[i]} rolled: {roll}")
    
    input("\nPress ENTER to continue...")

    # Still in the while gameover is False

    # Obtain the highest roll this round
    max_roll = max(current_rolls)

    # Winners will store information abow who won this round
    winners = []

    # Search for all players who got the highest roll
    for j in range(len(current_rolls)):
        if current_rolls[j] == max_roll:
            winners.append(player_names[j])
            player_wins[j] +=1
    
    print(f"Winners of this round are: {winners}")


    # Still in the while gameover is False

    # Check if someone reached winning score
    # (It is unlikely but there might be more than one winner)
    for z in range(number_of_players):
        if player_wins[z] >= winning_score:
            print(f"\n{player_names[z]} is the newest Battel of Dices Champion!")
            gameover = True

    if gameover is False:
        print("This heated Battle of Dices is still going on! Who will win in the end?")

    rounds += 1

# Save the results
filename = input("Enter the filename to save the results: ")
with open(filename, "w") as file: # "w" = write mode
    for round_number in range(rounds):
        file.write(f"Round {round_number+1}")
        rolls_str = "" # Start with an empty string
        for i in range(number_of_players):
                       rolls_str += (f"{player_names[i]} rolled {player_rolls_history[i][round_number]}")
                       if i < number_of_players - 1: # Add a comma after each, except the last one
                            rolls_str += ", "
        print(f"Saving {rolls_str}")

        file.write(rolls_str + "\n")


