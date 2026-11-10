def show_tender(tender_id,budget):
    print(f"Tender ID: {tender_id}")
    print(f"Budget: {budget}")

show_tender(101, 50000)
show_tender(102, 75000)

def calculate_total(price, quantity):
    total = price * quantity
    return total

result = calculate_total(250, 4)
print(result)

def calculate_profit(revenue, cost):
    profit = revenue - cost
    return profit

profit = calculate_profit(80000, 55000)

print(f"Profit: {profit} EUR")

def check_profit(revenue, cost):
    profit = revenue - cost
    if profit > 0:
        return "Profitable"
    else:
        return "Not profitable"

result_1 = check_profit(80000, 55000)
result_2 = check_profit(40000, 50000)

print(result_1)
print(result_2)

tender ={
    "id": 105,
    "revenue": 95000,
    "cost": 70000
}

def evaluate_tender(tender):
    profit = tender["revenue"] - tender["cost"]
    if profit > 0:
        return "Profitable"
    else:
        return "Not profitable"

profit = evaluate_tender(tender)

print(profit)