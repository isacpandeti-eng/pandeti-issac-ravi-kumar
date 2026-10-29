
months = ["January", "February", "March", "April"]
units_list = [80, 150, 260, 300]
bills = []

for i in range(len(units_list)):
    units = units_list[i]

    if units <= 100:
        energy = units * 2
    elif units <= 200:
        energy = 100 * 2 + (units - 100) * 3
    else:
        energy = 100 * 2 + 100 * 3 + (units - 200) * 5

    fixed = 50
    surcharge = energy * 0.05
    bill = energy + fixed + surcharge

    if units < 100:
        bill = bill - bill * 0.05

    bills.append(bill)

    print(months[i], "- Units:", units,
          "- Bill: Rs.", round(bill, 2))

print("\nUNUSUAL INCREASES")

for i in range(1, len(bills)):
    increase = bills[i] - bills[i - 1]

    if increase > 200:
        print(months[i], "bill increased by Rs.",
              round(increase, 2))

'''January - Units: 80 - Bill: Rs. 202.5
February - Units: 150 - Bill: Rs. 472.5
March - Units: 260 - Bill: Rs. 1155.0
April - Units: 300 - Bill: Rs. 1365.0

UNUSUAL INCREASES
March bill increased by Rs. 682.5
April bill increased by Rs. 210.0'''


flowchart TD
    A([Start]) --> B[Initialize months, units list and bills list]
    B --> C[Select next month and units]
    C --> D{Units <= 100?}
    D -- Yes --> E[Energy = Units x 2]
    D -- No --> F{Units <= 200?}
    F -- Yes --> G[Energy = 200 + Units above 100 x 3]
    F -- No --> H[Energy = 500 + Units above 200 x 5]
    E --> I[Add fixed charge and 5% surcharge]
    G --> I
    H --> I
    I --> J{Units < 100?}
    J -- Yes --> K[Apply 5% rebate]
    J -- No --> L[Store and display bill]
    K --> L
    L --> M{More months?}
    M -- Yes --> C
    M -- No --> N[Compare consecutive monthly bills]
    N --> O{Increase > Rs. 200?}
    O -- Yes --> P[Display unusual increase]
    O -- No --> Q{More comparisons?}
    P --> Q
    Q -- Yes --> N
    Q -- No --> R([Stop])
