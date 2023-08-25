#Boolean --> Elif

#create a variable called people and assign 40
people = 40
#create a variable called cars and assign 20
cars = 20
#create a variable called trucks and assign 25
trucks = 25

# More cars than people print(“We should take the cars.”)
if cars > people:
    print("We should take the cars.")
# Less cars than people print(“We should not take the cars.”)
elif cars < people:
    print("We should not take the cars.")
# Same number of cars and people print(“We can’t decide.”)
else:
    print("We can't decide.")

# Too many trucks print(“That’ s too many trucks.”)
if trucks > cars:
    print("That' s too many trucks.")
# Fewer trucks than cars print(“Maybe we could take the trucks.”)
elif trucks < cars:
    print("Maybe we could take the trucks.")
# Same number of trucks and cars print(“We still can’t decide.”)
else:
    print("We still can't decide.")

# More people than trucks print(“Alright, let’s just take the trucks.”)
if people > trucks:
    print("Alright, let's just take the trucks.")
# Less or equal people than trucks print(“Fine, let’s stay home then.”)
else:
    print("Fine, let's stay home then.")