class Student:
    def __init__(self, name, num):
        self.name = name
        self.num = num

students = []
students.append(Student("Bob", 1))
students.append(Student("Alice", 4))
students.append(Student("James", 3))
students.append(Student("Ray", 5))
students.append(Student("Lo", 6))
students.append(Student("Simon", 7))
students.append(Student("Tracy", 2))
students.append(Student("Lana", 8))

students.sort(key = lambda student: student.num)

for student in students:
    print(student.num, " ", student.name)