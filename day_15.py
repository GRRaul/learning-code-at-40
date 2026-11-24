"""
Day 11 Excersie 1 - Understanding list and dictionaries
"""
"""
markets = [
    {"country": "Spain", "sales": 150000, "growth": 12},
    {"country": "France", "sales": 120000, "growth": 8},
    {"country": "Germany", "sales": 200000, "growth": -3},
    {"country": "Italy", "sales": 95000, "growth": 15}
]

print(markets[0]['country'])
print(markets[2]['sales'])
print(markets[3]['growth'])

for market in markets:
    print(f"{market['country']}: {market['growth']}%")
"""



"""
Day 15 Exercise 2 - Functions and Arguments
- receive one market dictionary
- read its sales and growth values
- calculate the monetary increase or decrease in sales 
    - growth amount = (sales * growth) / 100
- return the calculated amount

Expected output
Spain: 18000.0
France: 9600.0
Germany: -6000.0
Italy: 14250.0
"""
"""
markets = [
    {"country": "Spain", "sales": 150000, "growth": 12},
    {"country": "France", "sales": 120000, "growth": 8},
    {"country": "Germany", "sales": 200000, "growth": -3},
    {"country": "Italy", "sales": 95000, "growth": 15}
]

def growth_amount(market):
    sales = market['sales']
    growth = market['growth']
    result = (sales * growth) / 100
    return result

best_country = None
highest_growth = float("-inf")

for market in markets:
    result = market['growth']
    if result > highest_growth:
        highest_growth = result
        best_country = market['country']

print(f"Highest growth: {best_country} {highest_growth}%")
"""
"""
Day 15 Excercise 3 comparing values and variable scope
- create best_country = None
- create highest_growth = float("-inf)
- use a for loop to examin each market
- compare its growth percentage against highest_growth
- update both variables whenever a higher percentage is found
- print the winning country and its grwoth percentage after the loop

Expected output
Highest growth: Italy (15%)
"""




"""
Exercise 4 Independent challenge
- create a function called classify_market(market) that return
- 10% or higher - High growth
- between 0% and 9% - Moderate growth
- below 0% - Declining
- prints the coumtry and its classification
- counts how many markets belong to each category
- prints the three total after the loop

Expected output
Spain: High growth
France: Moderate growth
Germany: Declining
Italy: High growth

High growth markets: 2
Moderate growth markets: 1
Declining markets: 1
"""

markets = [
    {"country": "Spain", "sales": 150000, "growth": 12},
    {"country": "France", "sales": 120000, "growth": 8},
    {"country": "Germany", "sales": 200000, "growth": -3},
    {"country": "Italy", "sales": 95000, "growth": 15}
]

def classify_market(market):
    growth = market['growth']
    if growth >= 10:
        return "High growth"
    elif growth >= 0:
        return "Moderate growth"
    else:
        return "Declining"


high_growth_market = 0
moderate_growth_market = 0
declining_market = 0

for market in markets:
    result = classify_market(market)
    if result == "High growth":
        high_growth_market += 1
    elif result == "Moderate growth":
        moderate_growth_market += 1
    elif result == "Declining":
        declining_market += 1
    country = market['country']
    print(f"{country}: {result}")

print(f"High growth markets: {high_growth_market}")
print(f"Moderate growth markets: {moderate_growth_market}")
print(f"Declining markets: {declining_market}")