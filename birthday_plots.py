'''

    Initialize the number of birthdays for each month to zero.
    Ask the user for the maximum number of birthdays for a month.
    Assign a random number between 0 and month-maximum for each month.
    Plot the results using pyplot. 
    
'''

import datetime
import random
import numpy as np
import matplotlib.pyplot as plt

random.seed(123)

months = ["january", "february", 
          "march", "april",
           "may", "june", 
          "july", "august", 
          "september", "october",
          "november", "december"]
max_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

plot_list  = []

for i, j in zip(months, max_days):
    while True:
        max_input = int(input(f"What is the maximum number of birthdays for {i}?  "))

        if max_input > j:
            print(f"Please input a number within the range of days in {i} (1 to {j}).")
        else:
            random_value = np.random.randint(low=0, high=max_input)
            plot_list.append(random_value)
            print("Nice!")
            break  # Exit the loop and move to the next month

# Plotting
plt.bar(x=months, height=plot_list, color='darkviolet', width=0.4)
plt.xlabel("Months")
plt.ylabel("Number of Birthdays")
plt.title("Number of Birthdays Per Month")
plt.grid()
plt.show()
