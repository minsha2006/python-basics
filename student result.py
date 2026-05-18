class Student:

    def __init__(self, name, roll, m1, m2, m3):
        self.name = name
        self.roll = roll
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def total(self):
        return self.m1 + self.m2 + self.m3

    def average(self):
        return self.total() / 3

    def grade(self):
        if self.average() >= 50:
            return "Pass"
        else:
            return "Fail"

    def display(self):
        print(self.name, self.roll)
        print("Total:", self.total())
        print("Average:", self.average())
        print("Grade:", self.grade())


s1 = Student("Rahul", 1, 80, 70, 90)
s2 = Student("Anu", 2, 95, 90, 85)

students = [s1, s2]

for s in students:
    s.display()
    print()

topper = s1

if s2.total() > topper.total():
    topper = s2

print("Topper:", topper.name)