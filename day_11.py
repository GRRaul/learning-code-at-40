"""
Day 11 Exercise 1 - Introducing try and except
- try - Python attempts to execute the code
- except - Python executes this block if the specified error occurs
"""
"""
revenue = 150000
cost = 110000

try:
    profit = revenue - cost
    print(profit)
except TypeError:
    print("Invalid data type")
"""
"""
What happens with this code?
"""
"""
revenue = "150000"
cost = 110000

try:
    profit = int(revenue) - cost
    print(profit)
except:
    print("Invalid data type")

"""
"""
The int() function converts a value into a integer when that conversin is possible
"""
"""
Python cannot convert "hello" into a integer, so it raises:
ValueError: invalid literal for int() with base 10: 'hello'
"""

"""
Add a second except bloc that catches Value Error and print:
Invalid numerical value
"""
"""
revenue = "hell0"
cost = 110000

try:
    profit = int(revenue) - cost
    print(profit)
except TypeError:
    print("Invalid data type")
except ValueError:
    print("Invalid numerical value")

"""

"""
Day 11 Exercise 2 - Validating Numerical Inputs
Modify convert_revenue(revenue) so that:
- it attempts to convert revenue into a integer using int()
- if the conversation succeeds, it returns the integer
- if a ValueError occurs, it returns 0
"""
"""
def convert_revenue(revenue):
    try:
        result = int(revenue)
        return result
    except ValueError:
        return 0

print(convert_revenue("150000"))
print(convert_revenue("unknown"))

"""




"""
Day 11 Exercise 3 - Functions and financial Calculations
Create a function called calcualte_profit(company) that :
- Converts revenue and cost into integers
- Calculates profit (revenue - cost)
- Returns the profit if both conversions succeed
- Returns 0 if either conversion raises a ValueError
Expected output
Global Industries: 40000
"""
"""
company = {
    "name": "Global Industries",
    "revenue": "150000", 
    "cost": "110000"
}

def calculate_profit(company):
    try:
        profit = int(company["revenue"]) - int(company["cost"])
        return profit
    except ValueError:
        return 0

print(calculate_profit(company))
"""




"""
Day 11 Excercise 4 - Independent Challenge
write a programem that:
- uses your existing calculate_profit(company) function
- loops through all companies
- displays each company's name and profit
- identifies the company with the highest profit
- handles invalid numerical values without crashing
Expected output:
Alpha Ltd: 40000
Beta Ltd: 0
Gamma Ltd: 75000
Delta Ltd: -10000

Best company: Gamma Ltd
Highest profit: 75000
"""

companies = [
    {"name": "Alpha Ltd", "revenue": "150000", "cost": "110000"},
    {"name": "Beta Ltd", "revenue": "unknown", "cost": "90000"},
    {"name": "Gamma Ltd", "revenue": "200000", "cost": "125000"},
    {"name": "Delta Ltd", "revenue": "95000", "cost": "105000"}
]
def calculate_profit(company):
    try:
        profit = int(company["revenue"]) - int(company["cost"])
        return profit
    except ValueError:
        return 0

for company in companies:
    profit = calculate_profit(company)
    print(f"{company['name']}: {profit}")

highest_profit = float("-inf")
best_company = None

for company in companies:
        profit = calculate_profit(company)
        if profit > highest_profit:
            highest_profit = profit
            best_company = company['name']

print(f"Best company: {best_company}")
print(f"Highest profit: {highest_profit}")