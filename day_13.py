"""
Day 13 Excercise 1 - Calculate profit margins
profit margin % = ((revenue - cost)/revenu ) * 100
the function must:
- receive the company dictionary
- calculate its profit
- calculate its profit margin as a percentage
- return the maring

Expected output
Profit margin: 30.0%
"""
"""
company = {
    "name": "Global Industries",
    "revenue": 0,
    "cost": 175000
}

def calculate_margin(company):
    if company['revenue'] <= 0:
        return 0
    else:
        profit = company['revenue'] - company['cost']
        margin = (profit / company['revenue']) * 100
        return margin

#print(f"Profit margin: {calculate_margin(company)}%")
"""

"""
Day 13 Excercise 2 - Analyse multiple companies
keeping calculate_margin(company) function unchanged
write a for loop that calls the function for each company an displays its name and profit margin

Expected output
Alpha Ltd: 25.0%
Beta Ltd: 30.0%
Gamma Ltd: 0%
Delta Ltd: 25.0%
"""
"""
companies = [
    {"name": "Alpha Ltd", "revenue": 200000, "cost": 150000},
    {"name": "Beta Ltd","revenue": 300000, "cost": 210000},
    {"name": "Gamma Ltd", "revenue": 0, "cost": 50000},
    {"name": "Delta Ltd", "revenue": 180000, "cost": 135000}
]

highest_margin = float("-inf")
best_company = None

for company in companies:
    result = calculate_margin(company)
    if result >  highest_margin:
        highest_margin = result
        best_company = company['name']
    print(f"{company['name']}: {result}%")

print(f"Best company: {best_company}")
print(f"Highest margin: {highest_margin}%")
"""    

"""
Identify Best company & Highest maring
Best company: Beta Ltd
Highest margin: 30.0%
"""




"""
Validate financial data
Calculate a function calculate_margin(company)
- converts revenue and cost into integers
- returns 0 if the conversion fails
- retunrs 0 if revenue is zero or negative
- otherwise, calculate and returns the profit margin
"""
companies = [
    {"name": "Alpha Ltd", "revenue": "200000", "cost": "150000"},
    {"name": "Beta Ltd", "revenue": "unknown", "cost": "210000"},
    {"name": "Gamma Ltd", "revenue": "0", "cost": "50000"},
    {"name": "Delta Ltd", "revenue": "180000", "cost": "135000"}
]
"""
def calculate_margin(company):
    try:
        revenue = int(company['revenue'])
        cost = int(company['cost'])
        if revenue <= 0:
            return 0
        profit = revenue - cost
        margin = (profit / revenue) * 100
        return margin
    except ValueError:
        return 0


for company in companies:
    print(calculate_margin(company))


"""


"""
Day 13 Exercise 4 - Independent Challenge
Build a programme
- uses your existing calculate_margin(company) funtction
- processes all five companies using one for loop
- print each company's name and margin
- identifies the company with the highest maring
- prints the best company and its margin

Expected output

Alpha Ltd: 30.0%
Beta Ltd: 0%
Gamma Ltd: 16,666666664%
Delta Ltd: 37.5%
Epsilon Ltd 0%

Best company: Delta Ltd
Highest margin: 37.5%
"""
companies = [
    {"name": "Alpha Ltd", "revenue": "250000", "cost": "175000"},
    {"name": "Beta Ltd", "revenue": "unknown", "cost": "120000"},
    {"name": "Gamma Ltd", "revenue": "180000", "cost": "150000"},
    {"name": "Delta Ltd", "revenue": "320000", "cost": "200000"},
    {"name": "Epsilon Ltd", "revenue": "0", "cost": "50000"}
]

def calculate_margin(company):
    try:
        revenue = int(company['revenue'])
        cost = int(company['cost'])
        if revenue <= 0:
            return 0
        profit = revenue - cost
        margin = (profit / revenue) * 100
        return margin
    except ValueError:
        return 0

highest_margin = float("-inf")
best_company = None

for company in companies:
    margin = calculate_margin(company)
    if margin > highest_margin:
        highest_margin = margin 
        best_company = company['name']
    print(f"{company['name']}: {margin:.2f}%")

print(f"Best company: {best_company}")
print(f"Highest margin: {highest_margin:.2f}%")