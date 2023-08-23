#Python Variables
# "=" assignment operator that assigns values for a given variable.

cars = 100   #Creates a variable called cars and assigns it a value of 100.
space_in_a_car = 4.0    #Creates a variable called space_in_a_car and assigns it a value of 4.0.
drivers = 30    #Creates a variable called drivers and assigns it a value of 30.
passengers = 90     #Creates a variable called passengers and assigns it a value of 90.  
cars_not_driven = cars - drivers    #Creates a variable called cars_not_driven and 
                                    #assigns it a value of difference of cars and drivers.
cars_driven = drivers      #Creates a variable called cars_driven and assigns it a value of drivers from the line 6.
carpool_capacity = cars_driven * space_in_a_car     #Creates a variable called carpool_capacity and 
                                                    #assigns it a value of product of cars_driven and space_in_car.
average_passengers_per_car = passengers / cars_driven      #Creates a variable called average_passengers_per_car and 
                                                            #assigns it a value of quotient of passenger and cars_driven.
age = 18

print("There are ", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car,
"in each car.")
print("I am", age)

#written by Abenezer Alemayehu