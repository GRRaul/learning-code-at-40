"""
Day 17 Updating dictionaries
- create the calculate_profit(company) function
- iterate through companies
- calculate each company's profit
- add the "profit" key directly to each existing dictionary
- print the complete list outside the loop

Expected output
[
    {'name': 'Apple', 'revenue': 350000, 'cost': 210000, 'profit': 140000},
    {'name': 'Amazon', 'revenue': 420000, 'cost': 380000, 'profit': 40000},
    {'name': 'Google', 'revenue': 280000, 'cost': 190000, 'profit': 90000},
    {'name': 'Netflix', 'revenue': 160000, 'cost': 180000, 'profit': -20000}
]
"""
"""
companies = [
    {"name": "Apple", "revenue": 350000, "cost": 210000},
    {"name": "Amazon", "revenue": 420000, "cost": 380000},
    {"name": "Google", "revenue": 280000, "cost": 190000},
    {"name": "Netflix", "revenue": 160000, "cost": 180000}
]

def calculate_profit(company):
    revenue = company["revenue"]
    cost = company["cost"]
    profit = revenue - cost
    return profit

for company in companies:
    profit = calculate_profit(company)
    company["profit"] = profit

print(companies)
"""



"""
Day 17 Exc. 2 Validating and Filtering Data
Combine error handling, dictionary updates and data filtering
- create an empty list called valid_companies
- create a function called calculate_profit(company)
- use try/except ValueError to handle invalid data
- convert revenue and cost into integers
- return the calculated profit if data is valid, or None if it is invalid
- iteare through the companies. if the returned value is not None, 
    add "profit" key to the dictionary and append the entire dictionary to
    valid_companies
- print the new list outside the loop

Expected output
[
    {'name': 'Apple', 'revenue': '350000', 'cost': '210000', 'profit': 140000},
    {'name': 'Google', 'revenue': '280000', 'cost': '190000', 'profit': 90000},
    {'name': 'Netflix', 'revenue': '160000', 'cost': '180000', 'profit': -20000}
]
"""
"""
companies = [
    {"name": "Apple", "revenue": "350000", "cost": "210000"},
    {"name": "Amazon", "revenue": "unknown", "cost": "380000"},
    {"name": "Google", "revenue": "280000", "cost": "190000"},
    {"name": "Netflix", "revenue": "160000", "cost": "180000"},
    {"name": "Microsoft", "revenue": "420000", "cost": "invalid"}
]

valid_companies = []

def calculate_profit(company):
    try:
        revenue = int(company["revenue"])
        cost = int(company["cost"])
        profit = revenue - cost
        return profit
    except ValueError:
        return None

for company in companies:
    profit = calculate_profit(company)
    if profit is not None:
        company["profit"] = profit
        valid_companies.append(company)

print(valid_companies)
"""



"""
Day 17 Exc. 3 Functions with Multiple Parameters
create a function that receives two parameters def check_profit(company, target):
- reuse calculate_profit(company) function
- return "Target achieved" if the profit is greater than or equal to the target
- otherwise, return "Belos target"
- iterate through the companies and call your function, passing both arguments
- add a new key called "status" to each original dictionary
- print each compnay's name and status

Expected output
Apple: Target achieved
Amazon: Below target
Google: Target achieved
Netflix: Below target

"""
"""
companies = [
    {"name": "Apple", "revenue": 350000, "cost": 210000},
    {"name": "Amazon", "revenue": 420000, "cost": 380000},
    {"name": "Google", "revenue": 280000, "cost": 190000},
    {"name": "Netflix", "revenue": 160000, "cost": 180000}
]

profit_target = 80000

def calculate_profit(company):
    try:
        revenue = int(company["revenue"])
        cost = int(company["cost"])
        profit = revenue - cost
        return profit
    except ValueError:
        return None

def check_profit(company, profit_target):
    profit = calculate_profit(company)
    if profit >= profit_target:
        return "Target achieved"
    else:
        return "Below target"

for company in companies:
    check = check_profit(company, profit_target)
    company["status"] = check
    print(company["name"], check)
"""



"""
Day 17 Exc. 4 Financial performance report
consolidate functions, multiple parameters, data validation, dictionary updates, filtering and counters
- create an empty list called successful_companies
- initialise three counters, one for each classificatin
- iterate through the companies
- calculate the profit using the first function
- pass the profit and target to the second function
- add a new key call status to each company dictionary
- append the names of successfull companies to the new list
- update the corresponding counters
- print each company's name and status
- print the three counters and the successful companies list

Expected output
Apple: Target achieved
Amazon: Below target
Google: Target achieved
Netflix: Below target
Microsoft: Invalid data
Meta: Target achieved

Target achieved: 3
Below target: 2
Invalid data: 1

Successful companies: ['Apple', 'Google', 'Meta']
"""

companies = [
    {"name": "Apple", "revenue": "350000", "cost": "210000"},
    {"name": "Amazon", "revenue": "420000", "cost": "380000"},
    {"name": "Google", "revenue": "280000", "cost": "190000"},
    {"name": "Netflix", "revenue": "160000", "cost": "180000"},
    {"name": "Microsoft", "revenue": "unknown", "cost": "250000"},
    {"name": "Meta", "revenue": "300000", "cost": "220000"}
]

profit_target = 80000

successful_companies = []

def company_profit(company):
    try:
        revenue = int(company["revenue"])
        cost = int(company["cost"])
        profit = revenue - cost
        return profit
    except ValueError:
        return None


target_achieve = 0
below_target = 0
invalid_data = 0

def company_check(profit, target):
   
    if profit is None:
        return "Invalid data"
    elif profit >= target:
        return "Target achieved"
    else:
        return "Below target"

for company in companies:
    profit = company_profit(company)
    result = company_check(profit, profit_target)        
    company["status"] = result
    print(f"{company["name"]}: {result}")
    if result == "Invalid data":
        invalid_data += 1
    elif result == "Target achieved":
        target_achieve += 1
        successful_companies.append(company["name"])
    else:
        below_target += 1

print(f"Target achieved: {target_achieve}")
print(f"Below target: {below_target}")
print(f"Invalid data: {invalid_data}")

print(successful_companies)