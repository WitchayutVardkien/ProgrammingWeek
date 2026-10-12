class Person:                                 
    def __init__(self, name, weight, height):
        self.name = name
        self.weight = weight                  
        self.height = height                 

    def getBMI(self):
        return self.weight / (self.height * self.height)

    def show(self):
        print("Name:", self.name, "Weight:", self.weight, "Height:", self.height)


class Student(Person):                          
    def __init__(self, name, weight, height, gpa):
        super().__init__(name, weight, height)   
        self.gpa = gpa                           

    def show(self):                            
        super().show()                          
        print("GPA:", self.gpa, "BMI:", round(self.getBMI(), 2))


class Employee(Person):
    def __init__(self, name, weight, height, salary):
        super().__init__(name, weight, height)
        self.salary = salary

    def show(self):
        super().show()
        print("Salary:", self.salary, "BMI:", round(self.getBMI(), 2))


s = Student("Mali", 50, 1.60, 3.25)
e = Employee("Somchai", 70, 1.75, 25000)
s.show()
e.show()
