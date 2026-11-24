"""
Day 16 Exercise 1 - Creating lists dynamically
.append() method
- create an empty list called company_names
- create a foor loop to iterate through companies
- extract each company´s name
- use .append() to store each name in your new list
- print the new list after the loop

Expected output
['Apple', 'Amazon', 'Google', 'Netflix']
"""
"""
companies = [
    {"name": "Apple", "revenue": 250000, "cost": 180000},
    {"name": "Amazon", "revenue": 320000, "cost": 240000},
    {"name": "Google", "revenue": 180000, "cost": 120000},
    {"name": "Netflix", "revenue": 150000, "cost": 110000}
]

company_name = []

def get_company_name(company):
    name = company['name']
    return name

for company in companies:
    name = get_company_name(company)
    company_name.append(name)

print(company_name)
"""



"""
Day Excersie 2 - Filtering Data
combine .append() with conditional statements to create a filtered list
- create an empty list called profitable_companies
- create a funtction called calculate_profit() that received one company dictionary
- calculate and retunr the profit (revenu - cost)
- iterate throguth the companis and call your function
- if the profit is greater than or equal to 60.000 append the compnany's name to the list
- print the new list outside the loop

Expected output
['Apple', 'Amazon', 'Google']
"""
"""
companies = [
    {"name": "Apple", "revenue": 250000, "cost": 180000},
    {"name": "Amazon", "revenue": 320000, "cost": 240000},
    {"name": "Google", "revenue": 180000, "cost": 120000},
    {"name": "Netflix", "revenue": 150000, "cost": 110000}
]

profitable_companies = []

def calculate_profit(company):
    revenue = company["revenue"]
    cost = company["cost"]
    profit = revenue - cost
    return profit

for company in companies:
    result = calculate_profit(company)
    if result >= 60000:
        profitable_companies.append(company["name"])
        

print(profitable_companies)
"""




"""
Day 16 Excercise 3 Create Dictionaries Dynamically
Create a new list containing the name and calculated profit of every company
- create an empty list called company_results
- reuse your calculate_profit(company) function
- iterate through the companies
- calculate each company's profit
- create a new dictionary containing its name and profit
- append the new dictionary to company_results
- print the complete list outside the loop

Expected output 
[
    {'name': 'Apple', 'profit': 70000},
    {'name': 'Amazon', 'profit': 80000},
    {'name': 'Google', 'profit': 60000},
    {'name': 'Netflix', 'profit': 40000}
]
"""
"""
def calculate_profit(company):
    revenue = company["revenue"]
    cost = company["cost"]
    profit = revenue - cost
    return profit

company_result = []

companies = [
    {"name": "Apple", "revenue": 250000, "cost": 180000},
    {"name": "Amazon", "revenue": 320000, "cost": 240000},
    {"name": "Google", "revenue": 180000, "cost": 120000},
    {"name": "Netflix", "revenue": 150000, "cost": 110000}
]

for company in companies:
    result = calculate_profit(company)
    to_add = {"name": company["name"], "profit": result}
    company_result.append(to_add)

print(company_result)
"""



"""
Day 16 Excercise 4 Independent Business Analysis
Combine functions, calculations, conditions, dictionaries and .append()
create a financial report containing only companies with a profit margin at least 25%
- create an empty list called financial_report
- create a function called calculate_margin(company)
- calculate and return the profit margin
- iterate through the companies
- if the profit margin is at least 25%, create a new dictionary containing company's name, profit and maring
- append that dictionary to financial_report
- print the complete report outside the loop
"""

companies = [
    {"name": "Apple", "revenue": 250000, "cost": 180000},
    {"name": "Amazon", "revenue": 320000, "cost": 240000},
    {"name": "Google", "revenue": 180000, "cost": 120000},
    {"name": "Netflix", "revenue": 150000, "cost": 110000}
]

def calculate_profit(company):
    revenue = company["revenue"]
    cost = company["cost"]
    profit = revenue - cost
    return profit

financial_report = []

def calculate_margin(company):
    profit = calculate_profit(company)
    revenue = company["revenue"]
    margin = (profit / revenue) * 100
    return margin

for company in companies:
    margin = calculate_margin(company)
    profit = calculate_profit(company)
    if margin >= 25:
        add_info = {"name": company['name'], "profit": profit, "margin": round(margin, 2)}
        financial_report.append(add_info)

print(financial_report)