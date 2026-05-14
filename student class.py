class Student:

    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display_details(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll_no)
        print("Marks:", self.marks)

    def calculate_average(self):
        average = sum(self.marks) / len(self.marks)
        print("Average Marks:", average)


s1 = Student("Rahul", 101, [80, 75, 90])

s1.display_details()
s1.calculate_average()