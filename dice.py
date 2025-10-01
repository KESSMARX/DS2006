import random

start = 1
stop = 20

# Run by pressing ENTER
input ("Please press ENTER to roll the dice!")

# Roll the dice
result = random.randint (start, stop)


# Show the result
print ("You rolled a", result, "out of a dice from", start, "to", stop)