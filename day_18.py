"""
Day 18 receive prodcut dictionary, calculate sales and return result
- receive the calculated sales and the target
- return "target achieved" or "Belos target"
- iterate throguh the prodcuts
- call the first function
- pass its returned value to the second function
- add two new keys to each dictionary: "sales" and "satus"
- print document name, sales and status

Expected output
Laptop: 54000 - Target achieved
Monitor: 42000 - Target achieved
Keyboard: 20000 - Below target
Mouse: 6000 - Below target
"""
"""
products = [
    {"name": "Laptop", "price": 1200, "units": 45},
    {"name": "Monitor", "price": 350, "units": 120},
    {"name": "Keyboard", "price": 80, "units": 250},
    {"name": "Mouse", "price": 40, "units": 150}
]

sales_target = 30000

def calculate_sales(product):
    price = product["price"]
    units = product["units"]
    sales = price * units
    return sales

def check_sales(sales, sales_target):
    if sales >= sales_target:
        return "Target achieved"
    else:
        return "Below target"

for product in products:
    sales = calculate_sales(product)
    result = check_sales(sales,sales_target)
    product["sales"] = sales
    product["status"] = result
    print(f"{product["name"]}: {sales} - {result}")
"""
    


"""
Day 18 Excerise 2 Local & global variables
Calculate and return the commission using comission = (sales * rate) / 100
- calculate the sales
- calculate the commission
- add both values to each product dictionary
- print the results

Expected output
Laptop: 54000 - Commission: 2700.0
Monitor: 42000 - Commission: 2100.0
Keyboard: 20000 - Commission: 1000.0
Mouse: 6000 - Commission: 300.0
"""
"""
products = [
    {"name": "Laptop", "price": 1200, "units": 45},
    {"name": "Monitor", "price": 350, "units": 120},
    {"name": "Keyboard", "price": 80, "units": 250},
    {"name": "Mouse", "price": 40, "units": 150}
]

commission_rate = 5

def calculate_sales(product):
    price = product["price"]
    units = product["units"]
    sales = price * units
    return sales

def commission_sales(sales, rate):
    commission = (sales * rate) / 100
    return commission

for product in products:
    rate = commission_rate
    sales = calculate_sales(product)
    commission = commission_sales(sales, rate)
    product["sales"] = sales
    product["commission"] = commission
    print(f"{product["name"]}: {product["sales"]}: Commission:{product["commission"]}")
"""




"""
Day 18 Excercise 3 reuse two existing functions and create a third one
calculate_nate_sales =(sales, commission)
- define the three functions
- iterate through the products
- execute the functions in the correct order
- compare net sales against net_sales_target inside the loop
- add four keys to each dictionary: "sales", "commission", "net_sales" "satus"
- print the results

Expected output
Laptop: 51300.0 - Target achieved
Monitor: 39900.0 - Below target
Keyboard: 19000.0 - Below target
Mouse: 5700.0 - Below target
"""
"""
products = [
    {"name": "Laptop", "price": 1200, "units": 45},
    {"name": "Monitor", "price": 350, "units": 120},
    {"name": "Keyboard", "price": 80, "units": 250},
    {"name": "Mouse", "price": 40, "units": 150}
]

commission_rate = 5
net_sales_target = 40000

def calculate_sales(product):
    price = product["price"]
    units = product["units"]
    sales = price * units
    return sales

def commission_sales(sales, commission_rate):
    commission = (sales * commission_rate) / 100
    return commission

def calculate_net_sales(sales, commission):
    net_sales = sales - commission
    return net_sales

def check_net_sales(net_sales, net_sales_target):
    if net_sales >= net_sales_target:
        return "Target achieved"
    else:
        return "Below target"

for product in products:
    sales = calculate_sales(product)
    commission = commission_sales(sales, commission_rate)
    net_sales = calculate_net_sales(sales, commission)
    status = check_net_sales(net_sales, net_sales_target)
    product["sales"] = sales
    product["commission"] = commission
    product["net sales"] = net_sales 
    product["status"] = status
    print(f"{product["name"]}: {product["net sales"]} - {product["status"]}")
    
    """



"""
Day 18 Excercise 4 Independent challenge
combine multiple functions, data validation, dictionary updates, counters and filtering without assistance
- validate the product data
- calculate sales, commission and net sales for valid prodcuts
- classify each product as Target achieved, Below target or Invalid data
- Update the product dictionaries with teh calculated values and status
- create a list containing the names of successful prodcuts
- count products in each of the three categories
- calculate the total net sales across all valid prodcuts
- print the final report

Expected output
Laptop: 51300.0 - Target achieved
Monitor: 39900.0 - Below target
Keyboard: 19000.0 - Below target
Mouse: 5700.0 - Below target
Tablet: Invalid data
Smartphone: 45600.0 - Target achieved

Target achieved: 2
Below target: 3
Invalid data: 1

Successful products: ['Laptop', 'Smartphone']

Total net sales: 161500.0
"""
products = [
    {"name": "Laptop", "price": "1200", "units": "45"},
    {"name": "Monitor", "price": "350", "units": "120"},
    {"name": "Keyboard", "price": "80", "units": "250"},
    {"name": "Mouse", "price": "40", "units": "150"},
    {"name": "Tablet", "price": "unknown", "units": "100"},
    {"name": "Smartphone", "price": "800", "units": "60"}
]

commission_rate = 5
net_sales_target = 40000

def calculate_sales(product):
    try:
        sales = int(product["price"]) * int(product["units"])
        return sales
    except ValueError:
        return None

def commission_sales(sales, commission_rate):
    commission_value = (sales * commission_rate) / 100
    return commission_value

def calculate_net_sales(sales, commission_value):
    net_sales = sales - commission_value
    return net_sales

def check_net_sales(net_sales, net_sales_target):
    if net_sales >= net_sales_target:
        return "Target achieved"
    else:
        return "Below target"

target_achieved = 0
below_target = 0
invalid_data = 0
total_net_sales = 0

successful_products = []

for product in products:
    sales = calculate_sales(product)
    if sales is None:
        invalid_data += 1
        product["status"] = "Invalid data"
        print(f"{product["name"]}: {product["status"]}")
    else:
        commission_value = commission_sales(sales, commission_rate)
        net_sales = calculate_net_sales(sales, commission_value)
        total_net_sales = total_net_sales + net_sales
        check_status = check_net_sales(net_sales, net_sales_target)
        product["sales"] = sales
        product["commission"] = commission_value
        product["net sales"] = net_sales
        product["status"] = check_status
        if check_status == "Target achieved":
            target_achieved += 1
            successful_products.append(product["name"])
        elif check_status == "Below target":
            below_target += 1
        print(f"{product["name"]}: {product["net sales"]} - {product["status"]} ")

print(f"Target achieved: {target_achieved}")
print(f"Below target: {below_target}")
print(f"Invalid data: {invalid_data}")

print(successful_products)

print(total_net_sales)



