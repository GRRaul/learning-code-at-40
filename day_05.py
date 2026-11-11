"""
Evaluate a tender
Challenge: Write a function called evaluate_tender() that:
1. Receives the tender dictionary as an argument.
2. Calculates the profit (revenue - cost).
3. Returns "Profitable" if the profit is greater than zero, otherwise "Not profitable".
4. Calls the function and prints the returned result.
"""

tender = {
    "id": 106,
    "revenue": 120000,
    "cost": 95000
}

def evaluate_tender(tender):
    profit = tender["revenue"] - tender["cost"]
    if profit > 0:
        return "Profitable"
    else:
        return "Not profitable"

profit = evaluate_tender(tender)

print(f"{profit}")


"""
Excercise 2
Task: Reuse your evaluate_tender() function and write a for loop that evaluates each tender.
"""

tenders = [
    {"id":101, "revenue":120000, "cost": 95000},
    {"id":102, "revenue":80000, "cost": 90000},
    {"id":103, "revenue":150000, "cost": 110000}
]

for tender in tenders:
    result = evaluate_tender(tender)
    print(f"{result}")

"""
Exercise 3
Task: Modify the loop so that it prints each tender's ID alongside its profitability status.
"""

for tender in tenders:
    result = evaluate_tender(tender)
    print(f"Tender {tender["id"]}: {result}")

"""
Exercsie 4
Task: Calculate the actual profit for each tender, rather than simply displaying whether it's profitable
"""

for tender in tenders:
    result = evaluate_tender(tender)
    profit = tender["revenue"] - tender["cost"]
    print(f"Tender {tender['id']}, Profit ={profit}")