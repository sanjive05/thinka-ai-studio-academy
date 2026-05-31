name = ""


class Student:
    name = ''
    age = 0
    grade = 0

    def __init__(self, student_name, student_age, student_grade):
        self.name = student_name
        self.age = student_age
        self.grade = student_grade

    def print_data(self):
        print(self.name, "  ", self.age, "  ", self.grade)


sanjive = Student("sanjive", 24, "5th")

sanjive.print_data()
