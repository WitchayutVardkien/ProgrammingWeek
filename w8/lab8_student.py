class Student:
    def __init__(self, name, age):   # constructor
        self.name = name
        self.age = age

    def show(self):                  # method
        print(self.name, self.age)


def youngest(students):
    young = students[0]
    i = 1
    while i < len(students):
        if students[i].age < young.age:
            young = students[i]
        i = i + 1
    young.show()


students = []
f = open("students.txt")
lines = f.readlines()
f.close()

i = 0
while i < len(lines):
    d = lines[i].split(",")
    students.append(Student(d[0], int(d[1])))
    i = i + 1

youngest(students)
