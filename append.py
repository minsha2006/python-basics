file_name = input("Enter the file name: ")

try:
    with open(file_name, "a") as file:
        name = input("Enter student name: ")
        roll_no = input("Enter roll number: ")
        marks = input("Enter marks: ")

        file.write(f"{name}, {roll_no}, {marks}\n")

    print("Student details appended successfully.")

except Exception as e:
    print("An error occurred:", e)