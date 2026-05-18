students = {
    "Arun": 85,
    "Meera": 92,
    "Rahul": 78,
    "Anu": 95
}

highest_marks = 0
topper = ""

for name in students:
    if students[name] > highest_marks:
        highest_marks = students[name]
        topper = name

print("Highest scorer:", topper)
print("Marks:", highest_marks)

