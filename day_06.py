"""
Excercise 1
Calculate a tender's profit. Write a function that returns the actual numerical profit
"""

tender = {
    "id": 201,
    "revenue": 175000,
    "cost": 132000,
}

def calculate_profit(tender):
    profit = tender["revenue"] - tender["cost"]
    return profit

result = calculate_profit(tender)

print(result)


"""
Excercise 2
Calculate the profit margin - Margin % =((revenue-cost)/Revenue)x100
"""

tender = {
    "id": 201,
    "revenue": 175000,
    "cost": 132000,
}

def calculate_margin(tender):
    margin = ((tender["revenue"] - tender["cost"]) / tender["revenue"]) * 100
    return margin

result = calculate_margin(tender)

print(f"{result:.2f}%")

"""
Exercise 3
Evaluate tender profitability
"""

tender = {
    "id": 201,
    "revenue": 175000,
    "cost": 132000,
}

def evaluate_margin(tender):
    margin = ((tender["revenue"] - tender ["cost"]) / tender["revenue"]) * 100
    if margin >= 20:
        return "High Margin"
    elif margin >= 10:
        return "Acceptable margin"
    else:
        return "Low margin"

result = evaluate_margin(tender)
print(f"{result}")

"""
Exercise 4
Evaluate Margins
"""

tenders = [
    {"id": 201, "revenue": 175000, "cost": 132000},
    {"id": 202, "revenue": 100000, "cost": 85000},
    {"id": 203, "revenue": 80000, "cost": 76000}
]

for tender in tenders:
    result = evaluate_margin(tender)
    print(f"Tender {tender['id']}: {result}")
    
