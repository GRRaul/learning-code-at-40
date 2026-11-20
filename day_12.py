"""
Day 12 - Excercise 1 
- Calculate and retunr the profit of the company passed to the function
- call the function separately for a company_a and company_b
- print both results, including each company's name

Expected output
Aplha Ltd: 40000
Beta Ltd: 75000
"""

company_a = {
    "name": "Alpha Ltd",
    "revenue": 150000,
    "cost": 110000
}

company_b = {
    "name": "Beta Ltd",
    "revenue": 200000,
    "cost": 125000
    }

"""
def company_profit(company):
    profit = company["revenue"] - company["cost"]
    return profit

#print(f"{company_a["name"]}: {company_profit(company_a)}")
#print(f"{company_b["name"]}: {company_profit(company_b)}")
"""

"""
Modify the futnion so that:
- it uses the global variable revenue
- it substract the local variable cost
it returns the calculated profit
you call the function and print the result
"""

revenue = 200000

"""
def calculate_profit():
    cost = 75000
    profit = revenue - cost
    return profit

#print(calculate_profit())
"""



"""
Day 12 - Excercise 3 - Funtions and loops
write a function called calculate_profit(company) that:
- receives one company dictionary as a parameter
- calculates its profits
- returns the result

Expected output
Alpha Ltd: 40000
Beta Ltd: 75000
Gamma Ltd: -10000
"""
"""
companies = [
    {"name": "Alpha Ltd", "revenue": 150000, "cost": 110000},
    {"name": "Beta Ltd", "revenue": 200000, "cost": 125000},
    {"name": "Gamma Ltd", "revenue": 95000, "cost": 105000}
]

def calculate_profit(company):
        profit = company['revenue'] - company['cost']
        return profit

highest_profit = float("-inf")
best_company = None

for company in companies:
     profit = calculate_profit(company)
     if profit > highest_profit:
            highest_profit = profit
            best_company = company['name']
     
print(f"{best_company}: {highest_profit}")


"""
"""
Let's find the company with the highest profit
"""





"""
Day 12 - Excercise 4 - Independent challenge
write a programme that:
- creates a function calculate_profit(product) that returns the profit of one product
- uses a for loop to process all prodcuts
- prints each product's names and profits
- idenfities the product's name and profit
- identifies the product with the highest profit
- prints the best product and its profit

Expected output
Product A: 15000
Product B: 25000
Product C: -5000
Product D: 35000

Best product: Product D
Highest profit: 35000
"""

products = [
    {"name": "Product A", "sales": 50000, "cost": 35000},
    {"name": "Product B", "sales": 80000, "cost": 55000},
    {"name": "Product C", "sales": 40000, "cost": 45000},
    {"name": "Product D", "sales": 95000, "cost": 60000}
]

def calculate_profit(product):
    profit = product['sales'] - product['cost']
    return profit

highest_profit = float("-inf")
best_product = None

for product in products:
    profit = calculate_profit(product)
    print(f"{product['name']}: {profit}")

    if profit > highest_profit:
        highest_profit = profit
        best_product = product['name']

print(f"Best product: {best_product}")
print(f"Highest profit: {highest_profit}")