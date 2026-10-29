
quantity = int(input("Enter production quantity: "))
material_per_unit = float(input("Material cost per unit: Rs. "))
labour_per_unit = float(input("Labour cost per unit: Rs. "))
machine_cost = float(input("Total machine cost: Rs. "))
wastage_rate = float(input("Wastage percentage: "))
selling_price = float(input("Selling price per unit: Rs. "))
target_profit = float(input("Target profit percentage: "))

if (quantity <= 0 or min(material_per_unit, labour_per_unit,
        machine_cost, wastage_rate, selling_price, target_profit) < 0
        or wastage_rate > 100):
    print("Invalid production details.")
else:
    material_cost = quantity * material_per_unit
    wastage_cost = material_cost * wastage_rate / 100
    labour_cost = quantity * labour_per_unit

    total_cost = material_cost + wastage_cost + labour_cost + machine_cost
    revenue = quantity * selling_price
    profit = revenue - total_cost

    if total_cost > 0:
        profit_percent = profit / total_cost * 100
    else:
        profit_percent = 0

    print("\n--- MANUFACTURING REPORT ---")
    print("Material Cost: Rs.", round(material_cost, 2))
    print("Wastage Cost: Rs.", round(wastage_cost, 2))
    print("Labour Cost: Rs.", round(labour_cost, 2))
    print("Machine Cost: Rs.", round(machine_cost, 2))
    print("Total Cost: Rs.", round(total_cost, 2))
    print("Sales Revenue: Rs.", round(revenue, 2))
    print("Profit/Loss: Rs.", round(profit, 2))
    print("Profit Percentage:", round(profit_percent, 2), "%")

    if profit < 0:
        print("Result: Production resulted in a loss.")
    elif profit_percent >= target_profit:
        print("Result: Target profit achieved.")
    else:
        print("Result: Target profit not achieved.")

'''Enter production quantity: 100
Material cost per unit: Rs. 50
Labour cost per unit: Rs. 20
Total machine cost: Rs. 1000
Wastage percentage: 5
Selling price per unit: Rs. 100
Target profit percentage: 20
--- MANUFACTURING REPORT ---
Material Cost: Rs. 5000.0
Wastage Cost: Rs. 250.0
Labour Cost: Rs. 2000.0
Machine Cost: Rs. 1000.0
Total Cost: Rs. 8250.0
Sales Revenue: Rs. 10000.0
Profit/Loss: Rs. 1750.0
Profit Percentage: 21.21 %
Result: Target profit achieved.'''

START

Input production and cost details
Are the inputs valid?
Yes
Calculate material, wastage, labour and total cost
Calculate revenue, profit and profit percentage
Is profit negative?
Yes
Display loss

No
Check target profit



No
Display invalid production details


Display manufacturing report and result
STOP