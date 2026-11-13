"""
Day 7 - Excercise 1
Build a Tender Analysis Tool - Reusing Functions
"""

tender = {
    "id": 301,
    "revenue": 200000,
    "cost": 150000
}

def calculate_profit(tender):
    profit = tender["revenue"] - tender["cost"]
    return profit

def calculate_margin(tender):
    profit = calculate_profit(tender)
    margin = (profit / tender["revenue"]) * 100
    return margin

result = calculate_margin(tender)
print(f"Margin: {result:.2f}%")

"""
Day 7 Excercise 2 - Return two values
Create a function called analyse_tender(tender) that:
Calls calculate_profit(tender)
Calss calculare_margin(tender)
Return both Values
"""

def analyse_tender(tender):
    profit = calculate_profit(tender)
    margin = calculate_margin(tender)
    return profit, margin

result = analyse_tender(tender)

print(f"Profit: {result[0]}")
print(f"Margin: {result[1]:.2f}%")

"""
Day 7 Exercise 3 Analyse multiple tenders
Combine three functions with a for loop
Calss analyse_tender(tender) for each one
Print the tender ID, profit and margin
"""

tenders =[
    {"id": 301, "revenue": 200000, "cost": 150000},
    {"id": 302, "revenue": 120000, "cost": 108000},
    {"id": 303, "revenue": 90000, "cost":85000}
]

for tender in tenders:
    result = analyse_tender(tender)
    print(f"Tender: {tender['id']}, Profit = {result[0]}, Margin = {result[1]:.2f}%")


"""
Day 7 Exercise 4 Find the most profitable tender
Comparing results
Goes through every tender using a for loop
Calculates the profit of each tender
indentifies which tender generates the highest profit
Prints the winning tender ID and its profit
"""

highest_profit = float ("-inf")
best_tender = None

for tender in tenders:
    result = analyse_tender(tender)
    if result[0] > highest_profit:
        highest_profit = result[0]
        best_tender = tender

print(f"Most profitable tender: {best_tender['id']}")
print(f"Profit: {highest_profit}")