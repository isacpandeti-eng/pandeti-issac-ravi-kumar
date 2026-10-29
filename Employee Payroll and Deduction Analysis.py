
name = input("Enter employee name: ")
basic = float(input("Enter basic salary: Rs. "))
allowances = float(input("Enter allowances: Rs. "))
overtime = float(input("Enter overtime pay: Rs. "))
incentives = float(input("Enter incentives: Rs. "))

if min(basic, allowances, overtime, incentives) < 0:
    print("Invalid salary details.")
else:
    gross = basic + allowances + overtime + incentives

    if gross <= 20000:
        tax = 0
    elif gross <= 40000:
        tax = (gross - 20000) * 0.05
    elif gross <= 60000:
        tax = 1000 + (gross - 40000) * 0.10
    else:
        tax = 3000 + (gross - 60000) * 0.15

    provident_fund = basic * 0.12
    total_deductions = tax + provident_fund
    net_salary = gross - total_deductions

    print("\n--- SALARY STATEMENT ---")
    print("Employee:", name)
    print("Basic Salary: Rs.", round(basic, 2))
    print("Allowances: Rs.", round(allowances, 2))
    print("Overtime: Rs.", round(overtime, 2))
    print("Incentives: Rs.", round(incentives, 2))
    print("Gross Salary: Rs.", round(gross, 2))
    print("Tax: Rs.", round(tax, 2))
    print("Provident Fund: Rs.", round(provident_fund, 2))
    print("Total Deductions: Rs.", round(total_deductions, 2))
    print("Net Salary: Rs.", round(net_salary, 2))
  
 ''' Enter employee name: Ravi
Enter basic salary: Rs. 30000
Enter allowances: Rs. 5000
Enter overtime pay: Rs. 2000
Enter incentives: Rs. 3000
--- SALARY STATEMENT ---
Employee: Ravi
Basic Salary: Rs. 30000.0
Allowances: Rs. 5000.0
Overtime: Rs. 2000.0
Incentives: Rs. 3000.0
Gross Salary: Rs. 40000.0
Tax: Rs. 1000.0
Provident Fund: Rs. 3600.0
Total Deductions: Rs. 4600.0
Net Salary: Rs. 35400.0


flowchart TD
    A([Start]) --> B[/Enter employee name and salary details/]
    B --> C{Any salary value negative?}
    C -- Yes --> D[Display Invalid salary details]
    D --> K([Stop])
    C -- No --> E[Calculate gross salary]
    E --> F{Gross salary <= 20000?}
    F -- Yes --> G[Tax = 0]
    F -- No --> H{Gross salary <= 40000?}
    H -- Yes --> I[Tax = 5% of amount above 20000]
    H -- No --> J{Gross salary <= 60000?}
    J -- Yes --> L[Tax = 1000 + 10% of amount above 40000]
    J -- No --> M[Tax = 3000 + 15% of amount above 60000]
    G --> N[Calculate PF = 12% of basic salary]
    I --> N
    L --> N
    M --> N
    N --> O[Calculate total deductions and net salary]
    O --> P[/Display salary statement/]
    P --> K'''
