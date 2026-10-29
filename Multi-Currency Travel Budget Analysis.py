
# Each row: category, amount in foreign currency, exchange rate to INR
expenses = [
    ["Hotel", 200, 85],
    ["Food", 100, 85],
    ["Transport", 50, 90],
    ["Shopping", 80, 85]
]

budget = float(input("Enter total travel budget in Rs.: "))
conversion_fee_rate = 0.02
total_expenses = 0
largest_category = ""
largest_amount = 0

print("\n--- TRAVEL EXPENSE REPORT ---")

for category, amount, exchange_rate in expenses:
    if amount < 0 or exchange_rate <= 0:
        print("Invalid expense:", category)
        continue

    converted = amount * exchange_rate
    fee = converted * conversion_fee_rate
    final_amount = converted + fee

    total_expenses = total_expenses + final_amount

    print(category, "- Converted: Rs.", round(converted, 2),
          "- Fee: Rs.", round(fee, 2),
          "- Total: Rs.", round(final_amount, 2))

    if final_amount > largest_amount:
        largest_amount = final_amount
        largest_category = category

print("\nTotal Expenses: Rs.", round(total_expenses, 2))
print("Budget: Rs.", round(budget, 2))
print("Largest Expense Category:", largest_category)

if total_expenses > budget:
    print("Budget exceeded by Rs.",
          round(total_expenses - budget, 2))
else:
    print("Budget remaining: Rs.",
          round(budget - total_expenses, 2))

'''Enter total travel budget in Rs.: 30000
   --- TRAVEL EXPENSE REPORT ---
Hotel - Converted: Rs. 17000 - Fee: Rs. 340 - Total: Rs. 17340
Food - Converted: Rs. 8500 - Fee: Rs. 170 - Total: Rs. 8670
Transport - Converted: Rs. 4500 - Fee: Rs. 90 - Total: Rs. 4590
Shopping - Converted: Rs. 6800 - Fee: Rs. 136 - Total: Rs. 6936

Total Expenses: Rs. 37536.0
Budget: Rs. 30000.0
Largest Expense Category: Hotel
Budget exceeded by Rs. 7536.0

'''
flowchart TD
    A([Start]) --> B[Initialize expense list and fee rate]
    B --> C[/Enter travel budget/]
    C --> D[Set total expenses and largest amount to zero]
    D --> E[Read next expense category, amount and exchange rate]
    E --> F{Amount < 0 or rate <= 0?}
    F -- Yes --> G[Display invalid expense]
    G --> M{More expenses?}
    F -- No --> H[Calculate converted amount]
    H --> I[Calculate 2% conversion fee]
    I --> J[Calculate final amount and update total]
    J --> K{Final amount > largest amount?}
    K -- Yes --> L[Update largest amount and category]
    K -- No --> M
    L --> M
    M -- Yes --> E
    M -- No --> N[Display total expenses and largest category]
    N --> O{Total expenses > budget?}
    O -- Yes --> P[Display budget exceeded amount]
    O -- No --> Q[Display remaining budget]
    P --> R([Stop])
    Q --> R
