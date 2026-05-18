import pandas as pd

data = {
    "Name": ["Arun", "Meera", "Rahul", "Anjali", "Vikram"],
    "Age": [20, 21, 19, 22, 20],
    "Marks": [85, 90, 78, 92, 88]
}

df = pd.DataFrame(data)

print("Students with Marks Above 80:")
print(df[df["Marks"] > 80])

print("\nStudents with Age Above 20:")
print(df[df["Age"] > 20])