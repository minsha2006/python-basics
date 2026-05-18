import pandas as pd

data = {
    "Name": ["Arun", "Meera", "Rahul", "Anjali", "Vikram"],
    "Age": [20, 21, 19, 22, 20],
    "Marks": [85, 90, 78, 92, 88]
}

df = pd.DataFrame(data)

df.to_csv("students.csv", index=False)

new_df = pd.read_csv("students.csv")

print("Data from CSV:")
print(new_df)

print("\nColumn Names:")
print(new_df.columns)

print("\nData Types:")
print(new_df.dtypes)