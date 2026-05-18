import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Name": ["Arun", "Meera", "Rahul", "Anjali", "Vikram",
             "Sneha", "Kiran", "Aditi", "Rohan", "Neha"],
    
    "Department": ["CS", "IT", "CS", "ECE", "IT",
                   "ECE", "CS", "IT", "ECE", "CS"],
    
    "Marks": [85, 90, 78, 92, 88,
              76, 95, 81, 69, 87],
    
    "Attendance": [82, 91, 70, 88, 74,
                   65, 96, 80, 72, 85]
}

df = pd.DataFrame(data)

print("Summary Statistics:")
print(df.describe())

df["Pass/Fail"] = np.where(df["Marks"] >= 75, "Pass", "Fail")

print("\nData with Pass/Fail Column:")
print(df)

df.to_csv("cleaned_students.csv", index=False)

plt.figure(figsize=(10, 6))
plt.bar(df["Name"], df["Marks"], color="skyblue")
plt.title("Student Marks Bar Chart")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(6, 6))
df["Department"].value_counts().plot.pie(autopct="%1.1f%%")
plt.title("Department Distribution")
plt.ylabel("")
plt.show()

plt.figure(figsize=(8, 5))
plt.hist(df["Marks"], bins=5, color="orange", edgecolor="black")
plt.title("Marks Distribution Histogram")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()

print("\nFinal Analysis Report:")
print("Total Students:", len(df))
print("Average Marks:", df["Marks"].mean())
print("Highest Marks:", df["Marks"].max())
print("Lowest Marks:", df["Marks"].min())
print("Pass Count:", len(df[df["Pass/Fail"] == "Pass"]))
print("Fail Count:", len(df[df["Pass/Fail"] == "Fail"]))