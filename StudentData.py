import pandas as pd

data = {
    "Name": ["Arun", "Meera", "Rahul", "Anjali", "Vikram"],
    "Age": [20, 21, 19, 22, 20],
    "Marks": [85, 90, 78, 92, 88]
}

df = pd.DataFrame(data)

print("DataFrame:")
print(df)

print("\nFirst 3 Rows:")
print(df.head(3))

print("\nShape:")
print(df.shape)