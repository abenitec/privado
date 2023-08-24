#Python: Libraries

# Import the choice function from the random module
from random import choice
# Import the randint function from the random module
from random import randint
# Import the shuffle function from the random module
from random import shuffle

# Generate a random integer between 1 and 10 and assign it to num
num = randint(1,10)
# Print the value of num
print(num)

# Choose a random element from the list ["heads", "tails"] and assign it to coin
coin = choice(["heads", "tails"])
# Print the value of coin
print(coin)

# Create a list of cards with "jack", "queen" and "king"
cards = ["jack", "queen", "king"]
# Shuffle the order of the elements in cards
shuffle(cards)
# Loop through each element in cards and print it
for card in cards:
    print(card)

# Create a list of friends with "Abenezer", "Abel" and "Abrham"
my_friends = ["Abenezer", "Abel", "Abrham"]
# Shuffle the order of the elements in my_friends
shuffle(my_friends)
# Loop through each element in my_friends and print it
for friend in my_friends:
    print(friend)
