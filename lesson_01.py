print("Hello, world!")
print("I´m learning Python")
print("My goal is to build AI-powered business applications")
print("I want to automate business processes")

unit_price = 250
quantity = 6
total = unit_price * quantity
print(total)
quantity = 10
total = unit_price * quantity
print(total)

company = "Barbera and Associates"
unit_price = 250.50
quantity = 10
is_eligible = True

print(type(company))
print(type(unit_price))
print(type(quantity))
print(type(is_eligible))

total = unit_price * quantity
print(f"Company: {company}")
print(f"Total offer: {total} EUR")

budget = 3000
if not is_eligible:
    print("Company is not eligible")
elif total > budget and is_eligible:
    print("Offer exceeds budget")
else:
    print("Offer can be submitted")


