#Python : Libraries

# Import the mean, median, mode, and variance functions from the statistics module
from statistics import mean
from statistics import mode
from statistics import median
from statistics import variance

# Define a list of ages
ages = [5, 10, 15, 20, 25]

# Calculate the mean of the ages using the mean() function
mean_age = mean(ages)
# Print the mean age
print(mean_age)

# Calculate the median of the ages using the median() function
median_age = median(ages)
# Print the median age
print(median_age)

# Calculate the mode of the ages using the mode() function
mode_age = mode(ages)
# Print the mode age
print(mode_age)

# Calculate the variance of the ages using the variance() function
variance_age = variance(ages)
# Print the variance of the ages
print(variance_age)