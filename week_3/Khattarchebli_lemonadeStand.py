"""
Author: Leslie Khattarchebli 
Date: 8/31/2025 
File Name: Khattarchebli_lemonadeStand.py 
Description: This file demonstrates basic python understanding
"""

#Function for calculating cost for making lemonade
def calculate_cost(lemons_cost, sugar_cost):
  total_cost = lemons_cost + sugar_cost
  return 

#Function for calculating the profits made for the lemonade stand
def calculate_profit (lemons_cost, sugar_cost, selling_price):
  total_cost = lemons_cost + sugar_cost
  profit = selling_price - total_cost
  return profit

#Variables to test
lemons_cost = 4
sugar_cost = 2
selling_price = 8

#Calculating costs and profits of lemonade stand
total_cost = f"(${lemons_cost}) + (${sugar_cost}) = (${calculate_cost(lemons_cost, sugar_cost)})"
profit = f"(${selling_price}) - (${lemons_cost} + ${sugar_cost}) = (${calculate_profit(lemons_cost, sugar_cost, selling_price)})"

cost_output = "Total cost: $" + str(total_cost)
profit_output = "Profit: $" + str(profit)

#Print results
print(cost_output)
print(profit_output)