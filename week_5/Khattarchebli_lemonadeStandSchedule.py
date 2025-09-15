""" 
Author: Leslie Khattarchebli 
Course: WEB-335 
Date: 9/14/2025 
File Name: Khattarchebli_lemonadeStandSchedule.py 
Description: This file demonstrates the use of both file header comments and normal 
level comments 
"""

tasks = ["Cut lemons", "Squeeze lemons", "Add water", "Set up stand", "Sell lemonade"]

# Using a for loop to iterate over the list
for task in tasks:
  print(task)  # Printing the task to the console

  # Days of the week
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

# Loop through each day
for i in range(len(days)):
    day = days[i]
    if day == "Saturday" or day == "Sunday":
        print(f"{day}: It's the weekend—time to rest!")
    else:
        print(f"{day}: Task - {tasks[i % len(tasks)]}")