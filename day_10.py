"""
Day 10 Exercise 1
Create a function called calculate_profit(company) that:
- Receives the company dictionary as an argument
- Calculates the profit by subtracting cost from revenue
- Returns the calculated profit
Expected output
Global Technologies
Profit: 53000
"""

company = {
    "name": "Global Technologies",
    "country": "United Kingdom",
    "revenue": 185000,
    "cost": 132000
}

def calculate_profit(company):
    profit = company["revenue"] - company["cost"]
    return profit

result = calculate_profit(company)

print(f"{company['name']}")
print (f"{result}")





"""
Day 10 Excercise 2 - Data Validation
Creat a function called validate_company(company) that checks:
- Revenue must be greater than 0
- Cost must be greater than or equal to 0
The function should return True if both conditions are satisfied, and False otherwise
"""

def validate_company(company):
    if company["revenue"] > 0 and company["cost"] >= 0:
        return True
    else:
        return False

result = validate_company(company)

print(f"{result}")





"""
Day 10 E3 - Loops and Financial Calculations
Write a for loop that:
- Goes through every company
- Calculates each company's profit
- Print the company name an its profits
Expected Output
Global Technologies: 53000
European Industries: -10000
Asian Manufacturing: 45000
"""

companies = [
    {"name": "Global Technologies", "revenue": 185000, "cost": 132000},
    {"name": "European Industries", "revenue": 95000, "cost": 105000},
    {"name": "Asian Manufacturing", "revenue": 220000, "cost":175000}
]
    

for company in companies:
    profit = company["revenue"] - company["cost"]
    print(f"{company['name']}: {profit}")





"""
Day 10 Excercise 4 Independent Challenge
Idenfify the company with the highest profit, using a function
- Create a function called find_best_company(companies)
- Loop through all companies
- Identify the company with the highest profit
- Return the company's name and its profit
- Print the resuts outside the function
Expected output
Best company: Global Technologies
Highest profit: 53000
"""



def find_best_company(companies):
    highest_profit = float("-inf")
    best_company = None
    for company in companies:
        profit = company["revenue"] - company["cost"]
        if profit > highest_profit:
            highest_profit = profit
            best_company = company["name"]

    return best_company, highest_profit

best_company, highest_profit = find_best_company(companies)

print(f"Best Company: {best_company}")
print(f"Highest profit: {highest_profit}")