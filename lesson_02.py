tender = "Analysing tender"

for number in range(1, 8):
    print(f"Tender {number}")

tender = "Tender"

for number in range(5, 11):
    print(f"{tender}{number}")

unit_price = 250

for quantity in range (1, 6):
    total = unit_price * quantity
    print(f"{quantity} units = {total} EUR")


total_value = 0
unit_price = 250


for number in range(1, 6):
    total_value = total_value + unit_price

print(f"{total_value} EUR")

unit_price = 175
total_value = 0

for number in range (1, 5):
    total_value = total_value + unit_price

print (f"{total_value} EUR")

document = 1

while document <= 5:
    print (f"Processing document {document}")
    document = document + 1


payment = 200
total = 0
payments_received = 0
target = 1000

while total < target:
    total = total + payment
    payments_received = payments_received + 1

print(f"Total received: {total} EUR")
print(f"Payments received: {payments_received}")

payment = 300
total = 0
payments_received = 0
target = 1200

while total < target:
    total = total + payment
    payments_received = payments_received + 1

print(f"Total received {total} EUR")
print(f"Payments received {payments_received}")

invoice = 1

while invoice <= 5:
        if invoice == 3:
            print(f"Invoice {invoice}: Manual review required")
        else:
            print(f"Invoice {invoice}: Ready")

        invoice = invoice +1


invoice = 1
manual_reviews = 0

while invoice <= 6:
    if  invoice == 2 or invoice == 5:
        manual_reviews = manual_reviews + 1
        print(f"Invoice {invoice}: Manual review required")
        
    else:
        print(f"Invoice {invoice}: Ready")

    invoice = invoice + 1

print(f"Total invoices requiring review: {manual_reviews}")


documents_required = 0

for number in range(1, 9):
    if number == 3 or number == 5 or number == 7:
        print(f" Tender {number}: Additional documents required")
        documents_required = documents_required + 1
    else:
        print(f" Tender {number}: Complete")

print(f"Total tenders requiring documents: {documents_required}")


tenders = [105, 210, 315, 420]

for tender in tenders:
    if tender == 315:
        print(f"Tender {tender}: Additional documents required")
    else:
        print(f"Tender {tender}: Complete")

tenders = [110, 220, 330, 440, 550]
print(f"First tender: {tenders[0]}")
print(f"Third tender: {tenders[2]}")
print(f"Last tender: {tenders[4]}")

prices = [150, 250, 350, 450]
prices[1] = 275
prices[3] = 500

for price in prices:
    print(f"Tender price: {price} EUR")


tenders = [100, 200]
tenders.append(300)
print(tenders)
print(len(tenders))

tenders = [110, 220, 330]

tenders.append(440)
tenders.append(550)

for tender in tenders:
    print(f"Registered tender: {tender}")

print(f"Total registered tenders: {len(tenders)}")

tender = {
    "id": 250,
    "company": "Barbera and Associates",
    "budget": 75000,
    "status": "Pending"
}
tender["status"] = "Approved"

print(tender["company"])
print(tender["budget"])
print(tender["status"])

tenders = [
    {"id": 101, "budget": 50000},
    {"id": 102, "budget": 75000},
    {"id": 103, "budget": 30000}
]

for tender in tenders:
    print(tender["budget"])

tenders = [
    {"id": 101, "budget": 50000},
    {"id": 102, "budget": 75000},
    {"id": 103, "budget": 30000}
]

total_budget = 0

for tender in tenders:
    total_budget = total_budget + tender["budget"]
    print(tender["budget"])

print(f"The total budget is {total_budget} EUR")

tenders = [
    {"id": 101, "budget": 50000},
    {"id": 102, "budget": 75000},
    {"id": 103, "budget": 30000},
    {"id": 104, "budget": 90000}
]

high_budget_count = 0

for tender in tenders:
    if tender["budget"] > 50000:
        print(f"Tender: {tender["id"]}")
        high_budget_count = high_budget_count +1

print(f"Total high-budget tenders: {high_budget_count}")

tenders = [
    {"id": 101, "budget": 50000, "status": "Pending"},
    {"id": 102, "budget": 75000, "status": "Approved"},
    {"id": 103, "budget": 90000, "status": "Pending"},
    {"id": 104, "budget": 120000, "status": "Pending"}
]

eligible_count = 0 

for tender in tenders:ju
    if tender["budget"] > 60000 and tender["status"] == "Pending":
        print(f"Eligible tender: {tender['id']}")
        eligible_count = eligible_count + 1

print(f"Total eligible tenders: {eligible_count}")