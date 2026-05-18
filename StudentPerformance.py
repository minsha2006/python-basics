import pandas as pd

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

print("Student DataFrame:")
print(df)

topper = df[df["Marks"] == df["Marks"].max()]

print("\nTopper:")
print(topper)

dept_avg = df.groupby("Department")["Marks"].mean()

print("\nAverage Marks Department-wise:")
print(dept_avg)

low_attendance = df[df["Attendance"] < 75]

print("\nStudents with Attendance Below 75%:")
print(low_attendance)

sorted_df = df.sort_values(by="Marks", ascending=False)

print("\nStudents Sorted by Marks (Descending):")
print(sorted_df)