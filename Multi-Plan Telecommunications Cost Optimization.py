
# (Plan name, monthly price, included data in GB, extra charge per GB)
plans = [
    ("Basic", 199, 2, 50),
    ("Standard", 399, 10, 30),
    ("Premium", 599, 25, 20)
]

usage = float(input("Enter monthly data usage in GB: "))
budget = float(input("Enter your budget: Rs. "))

best_plan = ""
best_cost = 0

print("\n--- PLAN COMPARISON ---")

if usage < 0 or budget < 0:
    print("Invalid usage or budget.")
else:
    for name, price, data, extra_rate in plans:
        if usage > data:
            extra_cost = (usage - data) * extra_rate
        else:START
        
        Initialize mobile plans
        Input data usage and budget
        Usage or budget is negative?
        No
        
        Calculate extra data charges and total cost for each plan
        Find the cheapest plan within budget
        Yes
        
        Display invalid input message
        Display best plan or no suitable plan
        STOP
        
        
            extra_cost = 0

        total = price + extra_cost

        print(name, "- Total cost: Rs.", round(total, 2))

        if total <= budget:
            if best_plan == "" or total < best_cost:
                best_plan = name
                best_cost = total

    if best_plan != "":
        print("\nBest Plan:", best_plan)
        print("Monthly Cost: Rs.", round(best_cost, 2))
    else:
        print("\nNo plan fits your budget.")

'''Enter monthly data usage in GB: 12
Enter your budget: Rs. 700
--- PLAN COMPARISON ---
Basic - Total cost: Rs. 699.0
Standard - Total cost: Rs. 459.0
Premium - Total cost: Rs. 599.0

Best Plan: Standard
Monthly Cost: Rs. 459.0'''

START

Initialize mobile plans
Input data usage and budget
Usage or budget is negative?
No
Calculate extra data charges and total cost for each plan
Find the cheapest plan within budget

Yes
Display invalid input message


Display best plan or no suitable plan
STOP








