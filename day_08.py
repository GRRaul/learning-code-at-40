"""
Day 08 - Excercise 1
Use dictionary to:
Check whether revenue is greater than zero
If it is, calculates the profit (revenue - cost)
Prints the compnay name and canculate profit
Othwerise, prints "Invalid revenue"
"""

company = {
    "name": "Global Industries",
    "country": "Spain",
    "revenue": 0,
    "cost": 110000
}

def company_revenue(company):
    revenue = company['revenue']
    if revenue > 0:
        return revenue
    else:
        return 0
        #print(f"revenue is greater than 0")

company_revenue(company)

def company_profit(company):
    profit = (company['revenue'] - company['cost'])
    return profit
    #print(profit)

revenue = company_revenue(company)
profit = company_profit(company)

if revenue > 0:
    print(f"{company['name']} {profit}")
else:
    print("Invalid revenue")



"""
Day 8 Exercise 2
Practise functions, return and conditional logic
Create a function called validate_company(company)
- Checks whether revenue is greater than zero
- Checks whether cost is greater or equal to zero
- Return True if both conditions are satisfied
- Otherwise, return False
"""

company = {
    "name": "Global Industries",
    "country": "Spain",
    "revenue": 150000,
    "cost": 0
}

def validate_company(company):
    if company['revenue'] > 0 and company['cost'] >= 0:
        return True
    else:
        return False

result = validate_company(company)
print(f"{result}")

"""
Day 08 Exercise 3
Practise loops, lists, dictionaries and functios together
Loop through the compannies
Print only the name of each company
"""

companies = [
    {"name": "Global Industries", "revenue": 150000, "cost":110000},
    {"name": "European Trading", "revenue": 0, "cost": 50000},
    {"name": "Asian Manufacturing", "revenue": 220000, "cost": 170000}
]

def company_name(companies):
    for company in companies:
        if company['revenue'] > 0:
            profit = company['revenue'] - company['cost']
            print(f"{company['name']}: {profit} ")
        else:
            print("Invalid company")

company_name(companies)

"""
Combine the loop with the validation function form Exercise 2
Modify company_name() so that:
- If a compnay's revenue is greater than 0, prints name
- Otherwise, print "Invalid company"
"""
"""
If revenue is greater than 0, calculate the compnay´s profit
Print the compnay name and its profit
Otherwise, print "Invalid Company"
"""

"""
Day 08 - Exercise 4
Independent Challenge - Find the most profitable valid company
- Loop through all companies
- Ignore compnaies with revenue less than or equal to zero
- Calculate profit of each valid company
- Identify the compnay with the highest profit
- Print its name and profit
"""

companies = [
    {"name": "Global Industries", "revenue": 150000, "cost":110000},
    {"name": "European Trading", "revenue": 0, "cost": 50000},
    {"name": "Asian Manufacturing", "revenue": 220000, "cost": 170000}
]

highest_profit = float("-inf")
best_company = None

for company in companies:
    if company['revenue'] >0:
        profit = company['revenue'] - company['cost']
        if profit > highest_profit:
            highest_profit = profit 
            best_company = company['name']

print(f"{best_company}: {highest_profit}")