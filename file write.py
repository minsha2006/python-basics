name = input("Enter student name: ")
age = input("Enter student age: ")
marks = input("Enter student marks: ")

file = open("student_details.txt", "w")

file.write("Student Details\n")
file.write("Name: " + name + "\n")
file.write("Age: " + age + "\n")
file.write("Marks: " + marks + "\n")

file.close()

print("Student details saved successfully.")