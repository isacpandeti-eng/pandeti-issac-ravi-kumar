
venue = float(input("Enter venue cost: Rs. "))
equipment = float(input("Enter equipment cost: Rs. "))
catering_per_person = float(input("Catering cost per person: Rs. "))
transport = float(input("Enter transport cost: Rs. "))
certificate_per_person = float(input("Certificate cost per person: Rs. "))
sponsorship = float(input("Enter sponsorship amount: Rs. "))
fee = float(input("Registration fee per person: Rs. "))
participants = int(input("Expected number of participants: "))

if (min(venue, equipment, catering_per_person, transport,
        certificate_per_person, sponsorship, fee) < 0
        or participants < 0):
    print("Invalid input.")
else:
    fixed_cost = venue + equipment + transport
    variable_cost = catering_per_person + certificate_per_person

    total_cost = fixed_cost + variable_cost * participants
    registration_income = fee * participants
    total_income = registration_income + sponsorship
    shortfall = total_cost - total_income

    # Find the minimum registrations needed to break even
    if fee <= variable_cost:
        minimum_registrations = -1
    else:
        minimum_registrations = 0

        while (fixed_cost + variable_cost * minimum_registrations
               > sponsorship + fee * minimum_registrations):
            minimum_registrations += 1

    print("\n--- CAMPUS EVENT FINANCIAL REPORT ---")
    print("Fixed Costs: Rs.", round(fixed_cost, 2))
    print("Variable Cost per Participant: Rs.",
          round(variable_cost, 2))
    print("Total Event Cost: Rs.", round(total_cost, 2))
    print("Registration Income: Rs.", round(registration_income, 2))
    print("Sponsorship: Rs.", round(sponsorship, 2))
    print("Total Income: Rs.", round(total_income, 2))

    if shortfall > 0:
        print("Funding Shortfall: Rs.", round(shortfall, 2))
    else:
        print("Surplus: Rs.", round(-shortfall, 2))

    if minimum_registrations == -1:
        print("Break-even is not possible with this fee.")
    else:
        print("Minimum Registrations for Break-even:",
              minimum_registrations)

'''Enter venue cost: Rs. 10000
Enter equipment cost: Rs. 5000
Catering cost per person: Rs. 200
Enter transport cost: Rs. 3000
Certificate cost per person: Rs. 50
Enter sponsorship amount: Rs. 10000
Registration fee per person: Rs. 500
Expected number of participants: 50
--- CAMPUS EVENT FINANCIAL REPORT ---
Fixed Costs: Rs. 18000.0
Variable Cost per Participant: Rs. 250.0
Total Event Cost: Rs. 30500.0
Registration Income: Rs. 25000.0
Sponsorship: Rs. 10000.0
Total Income: Rs. 35000.0
Surplus: Rs. 4500.0
Minimum Registrations for Break-even: 32
## 1. Scholarship Allocation – Algorithm

Step 1: Start the program.

Step 2: Store student details, including name, aggregate marks, Mathematics marks, Science marks, attendance, and family income.

Step 3: Check each student's eligibility:

- Aggregate marks ≥ 80
- Mathematics marks ≥ 60
- Science marks ≥ 60
- Attendance ≥ 75%
- Family income ≤ ₹3,00,000

Step 4: Add eligible students to the eligible list.

Step 5: Sort eligible students by aggregate marks in descending order and then attendance in descending order.

Step 6: Display each eligible student's rank, name, marks, attendance, and income.

Step 7: If no students qualify, display “No eligible students found.”

Step 8: Stop the program.

## 2. Scholarship Allocation – Flowchart


flowchart TD
    A([Start]) --> B[Enter student details]
    B --> C{Aggregate >= 80, Math >= 60, Science >= 60, Attendance >= 75, Income <= 300000?}
    C -- Yes --> D[Add student to eligible list]
    C -- No --> E{More students?}
    D --> E
    E -- Yes --> B
    E -- No --> F[Sort eligible students by marks and attendance]
    F --> G{Eligible list empty?}
    G -- Yes --> H[Display No eligible students found]
    G -- No --> I[Display ranked student details]
    H --> J([Stop])
    I --> J

Note: In the original Python code, Sita's attendance is 85%, while Ravi's is 80%. Therefore, Sita should rank first because both have 90 aggregate marks. The output you shared should be corrected accordingly.'''