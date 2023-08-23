#Conditionals

#create a variable called people and assigns value 40
people = 40
#create a variable called cats and assigns value 30
cats = 30
#create a variable called dogs and assigns value 15
dogs = 15

#If the number of cats is greater than the number of people it will print "Too many cats! The world is doomed!"
if people < cats:
    print("Too many cats! The world is doomed!")
#If the number of people is greater than the number of cats it will print "Not many cats! The world is saved!"
if people > cats:
    print("Not many cats! The world is saved!")
#If the number of dogs is greater than the number of people it will print "The world is drooled on!"
if people < dogs:
    print("The world is drooled on!")
#If the number of people is greater than the number of dogs it will print "The world is dry!"   
if people > dogs:
    print("The world is dry!")

#add 25 for the value of dogs so now dogs = 40 a
dogs += 25

#If the number of people is greater than or equal to the number of dogs it will print "People are greater than or equal to dogs."
if people >= dogs:
    print("People are greater than or equal to dogs.")
#If the number of dogs is greater than the number of people it will print "People are less than or equal to dogs."
if people <= dogs:
    print("People are less than or equal to dogs.")
#If the number of people is equal to the number of dogs it will print "People are dogs."
if people == dogs:
    print("People are dogs.")