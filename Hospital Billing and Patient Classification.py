
name = input("Enter patient name: ")
age = int(input("Enter patient age: "))
consultation = float(input("Consultation charges: Rs. "))
diagnostic = float(input("Diagnostic charges: Rs. "))
treatment = float(input("Treatment charges: Rs. "))

if age < 0 or consultation < 0 or diagnostic < 0 or treatment < 0:
    print("Invalid input. Values cannot be negative.")
else:
    total = consultation + diagnostic + treatment

    if age >= 60:
        concession = total * 0.10
    else:
        concession = 0

    final_bill = total - concession

    if final_bill < 1000:
        category = "Low Bill"
    elif final_bill <= 5000:
        category = "Medium Bill"
    else:
        category = "High Bill"

    print("\n--- HOSPITAL BILL ---")
    print("Patient:", name)
    print("Total Charges: Rs.", round(total, 2))
    print("Concession: Rs.", round(concession, 2))
    print("Final Bill: Rs.", round(final_bill, 2))
    print("Patient Classification:", category)

'''Enter patient name: Ravi
Enter patient age: 65
Consultation charges: Rs. 500
Diagnostic charges: Rs. 1000
Treatment charges: Rs. 3000
--- HOSPITAL BILL ---
Patient: Ravi
Total Charges: Rs. 4500.0
Concession: Rs. 450.0
Final Bill: Rs. 4050.0
Patient Classification: Medium Bill'''

START

Input patient details and charges
Are any values negative?
Yes
Display invalid input

No
Calculate total charges
Age 60 or above?
Yes
10% concession

No
No concession


Calculate final bill and classify


Display hospital bill
STOP