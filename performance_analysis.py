
# Student Performance Data Analysis
# Created by Subhasree S.

students = [
    {"name": "Anu", "marks": 85},
    {"name": "Bala", "marks": 72},
    {"name": "Charan", "marks": 91},
    {"name": "Divya", "marks": 68},
    {"name": "Ezhil", "marks": 78}
]

print("===== STUDENT PERFORMANCE ANALYSIS =====")

total = 0
highest = students[0]

print("\nStudent Marks Report")
print("--------------------")

for student in students:
    name = student["name"]
    marks = student["marks"]
    total += marks

    if marks > highest["marks"]:
        highest = student

    status = "Pass" if marks >= 35 else "Fail"
    print(f"{name}: {marks}/100 - {status}")

average = total / len(students)

print("\n===== SUMMARY =====")
print(f"Number of Students: {len(students)}")
print(f"Total Marks: {total}")
print(f"Average Marks: {average:.2f}")
print(
    f"Highest Scorer: {highest['name']} "
    f"({highest['marks']} marks)"
)
