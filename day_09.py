"""
Day 09 Excercise 1 Understanding return
"""

def calculate_profit(revenue, cost):
    profit = revenue - cost
    return profit

result = calculate_profit(150000, 110000)

print(result)

"""
Modify your functin so
- it uses return instead of prinft()
- the final print (result) remains unchanged
- the programme displays only 40000
"""

"""
Day 9 - Excercise 2 - Variable Scope
Understan the difference between local and global variables
"""


def calculate_profit(revenue, cost):
    profit = revenue - cost
    return profit

result = calculate_profit(150000, 110000)

print(result)






"""
Day 9 - Exercise 3 - Tracking values inside loops
Understand how a variable changes during each iteration of a for loop
"""

profits = [-10000, -5000, -15000]

highest_profit = float("-inf")

for profit in profits:
    if profit > highest_profit:
        highest_profit = profit

print(highest_profit)

"""
Indentation 
- move print(highest_profit) outside the for loop
- move print(highest-profit) inside the for loop, below higest_profit
"""




"""
Day 9 Excercise 4 - Independent Challenge
combine functions, return, loops, conditions and variable scope
objective, creat a function called find_highest_profit(profits) that find and return highest profit
Expected output - Highest profit: 25000
"""

profits = [12000, -5000, 25000, 18000, -2000]

def find_highest_profit(profits):
    highest_profit = float("-inf")
    for profit in profits:
        if profit > highest_profit:
            highest_profit = profit
            
    return highest_profit

result = find_highest_profit(profits)

print(f"Highest profit: {result}")