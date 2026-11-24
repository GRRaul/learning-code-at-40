"""
Day 14 Excercise 1 - Functions, dictionaries and loops
- receive one country dictinary as a parameter
- calculate total sales (q1 + q2)
- return the result using return
- use a for loop to call the function for every country
- print the country name and its total sales
- def calculate_total_sales(country):

Expected output
Spain: 265000
France: 205000
Germany: 355000
Italy: 185000
"""
"""
sales = [
    {"country": "Spain", "q1": 120000, "q2": 145000},
    {"country": "France", "q1": 95000, "q2": 110000},
    {"country": "Germany", "q1": 180000, "q2": 175000},
    {"country": "Italy", "q1": 80000, "q2": 105000}
]

def calculate_sales(sales):
    country_sale = sales['q1'] + sales['q2']
    return country_sale

best_country = None
highest_sales = float("-inf")

for sale in sales:
    country_sale = calculate_sales(sale)
    print(f"{sale['country']} {country_sale}")
    if country_sale > highest_sales:
        highest_sales = country_sale
        best_country = sale['country']

print(f"Best country: {best_country}")
print(f"Highest sales: {highest_sales}")
"""
"""
Day 14 Excersie 2 Sales target
- create a function check_target(country)
- use a for loop to display
Spain: Achieved
France: Not achieved
Germany: Achieved
Italy: Not achieved
"""
"""
countries = [
    {"name": "Spain", "sales": 265000, "target": 250000},
    {"name": "France", "sales": 205000, "target": 220000},
    {"name": "Germany", "sales": 355000, "target": 350000},
    {"name": "Italy", "sales": 185000, "target": 200000}
]

target_achieved = 0
target_not_achieved = 0

def check_target(country):
    if country['sales'] >= country['target']:
        return "Achieved"
    else:
        return "Not achieved"

for country in countries:
    result = check_target(country)
    if result == "Achieved":
        target_achieved += 1
    elif result == "Not achieved":
        target_not_achieved += 1
    
    print(f"{country['name']}: {result}")

print(f"Target achieved:{target_achieved}")
print(f"Target not achieved:{target_not_achieved}")
"""
"""
Combine function with an accumulator
- count how many countries achieved their targets
- count how many countries did not achieve their targets
- print each country´s result as before
- print both totals after the loop

Expected output
Spain: Achieved
France: Not achieved
Germany: Achieved
Italy: Not achieved

Targets achieved: 2
Targets not achieved: 2
"""




"""
Day 14 Exercise 3 - Data Validation - try/except
- convert sales and target into integers
- use try/except to handle invalid values
- return "Achieved" if sales are greater than or equal to the target
- return "Not achieved" if sales are below the target
- return "Invalid data" if conversatin fails

Expected output
Spain: Achieved
France: Invalid data
Germany: Achieved
Italy: Invalid data
"""
"""
countries = [
    {"name": "Spain", "sales": "265000", "target": "250000"},
    {"name": "France", "sales": "unknown", "target": "220000"},
    {"name": "Germany", "sales": "355000", "target": "350000"},
    {"name": "Italy", "sales": "185000", "target": "invalid"}
]

def check_target(country):
    try:
        sales = int(country['sales'])
        target = int(country['target'])
        if sales >= target:
            return "Achieved"
        else:
            return "Not achieved"
    except ValueError:
        return "Invalid data"
            
achieved = 0
not_achieved = 0
invalid_data = 0

for country in countries:
    result = check_target(country)
    if result == "Achieved":
        achieved += 1
    elif result == "Not achieved":
        not_achieved += 1
    elif result == "Invalid data":
        invalid_data += 1

    print(f"{country['name']}: {result}")

print(f"Achieved: {achieved}")
print(f"Not achieved: {not_achieved}")
print(f"Invalid data: {invalid_data}")
"""




"""
Day 14 - Excersie 4 - Independent Challenge - Inventory Management
- creates a function called check_stock(product)
- convert stock and minumun into integerts
- returns "Sufficient" if stock is greater than or equal to the minimum
- returns "Low stock" if stock is below the minumum
- returns "Invalid data" if conversion fails
- uses one loop to process all products
- counts how many products belos to each category

Expected output 
Laptop: Sufficient
Monitor: Low stock
Keyboard: Invalid data
Mouse: Sufficient
Printer: Low stock

Sufficient: 2
Low stock: 2
Invalid data: 1
"""

products = [
    {"name": "Laptop", "stock": "15", "minimum": "10"},
    {"name": "Monitor", "stock": "5", "minimum": "8"},
    {"name": "Keyboard", "stock": "unknown", "minimum": "20"},
    {"name": "Mouse", "stock": "25", "minimum": "15"},
    {"name": "Printer", "stock": "3", "minimum": "5"}
]

def check_stock(product):
    try:
        stock = int(product['stock'])
        minimum = int(product['minimum'])
        if stock >= minimum:
            return "Sufficient"
        elif stock < minimum:
            return "Low stock"
    except ValueError:
        return "Invalid data"

sufficient = 0
low_stock = 0
invalid_data = 0

for product in products:
    result = check_stock(product)
    if result == "Sufficient":
        sufficient += 1
    elif result == "Low stock":
        low_stock += 1
    elif result == "Invalid data":
        invalid_data += 1
    print(f"{product['name']}: {result}")

print(f"Sufficient: {sufficient}")
print(f"Low Stock: {low_stock}")
print(f"Invalid data: {invalid_data}")

