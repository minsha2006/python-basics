import pandas as pd
import numpy as np

data = {
    "Name": ["Arun", "Meera", "Rahul", "Anjali", "Vikram"],
    "Age": [20, 21, np.nan, 22, 20],
    "Marks": [85, np.nan, 78, 92, 88]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

print("\nMissing Values:")
print(df.isnull())

filled_df = df.fillna({
    "Age": df["Age"].mean(),
    "Marks": df["Marks"].mean()
})

print("\nDataFrame After Filling Missing Values:")
print(filled_df)

dropped_df = df.dropna()

print("\nDataFrame After Removing Missing Rows:")
print(dropped_df)