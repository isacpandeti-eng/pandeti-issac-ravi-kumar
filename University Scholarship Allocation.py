
students = [
    ("Ravi", 90, 85, 92, 80, 200000),
    ("Sita", 90, 80, 88, 85, 250000),
    ("Arun", 75, 70, 80, 78, 180000),
    ("Priya", 85, 65, 90, 82, 280000),
    ("Kiran", 88, 75, 70, 80, 400000)
]

eligible = []

for name, aggregate, math, science, attendance, income in students:
    if (aggregate >= 80 and math >= 60 and science >= 60
            and attendance >= 75 and income <= 300000):
        eligible.append(
            (name, aggregate, attendance, income)
        )

# Sort by aggregate descending, then attendance descending
eligible.sort(key=lambda s: (s[1], s[2]), reverse=True)

print("SCHOLARSHIP ELIGIBLE STUDENTS")
print("-" * 55)

rank = 1
for name, marks, attendance, income in eligible:
    print("Rank:", rank, "| Name:", name,
          "| Marks:", marks,
          "| Attendance:", attendance,
          "| Income:", income)
    rank += 1

if len(eligible) == 0:
    print("No eligible students found.")

'''SCHOLARSHIP ELIGIBLE STUDENTS
-------------------------------------------------------
Rank: 1 | Name: Ravi | Marks: 90 | Attendance: 80 | Income: 200000
Rank: 2 | Name: Sita | Marks: 90 | Attendance: 80 | Income: 250000
Rank: 3 | Name: Priya | Marks: 85 | Attendance: 82 | Income: 280000'''