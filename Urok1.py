class Student:
    numor = 0
    print("Hellow world")
    def __init__(self, height = 164):
        self.height = height
        Student.number = Student.number + 1
    def grow(self, height = 3):
        self.height = self.height + height
    def __str__(self):
        return f"я студент з іменем {self.name} Мій зріст {self.height}"

Artem = Student(height=178)
Mark = Student()

print("My height = ", Artem.height)
print("My height = ", Mark.height)

while Mark.height < 180:
    Mark.grow()
print("My height = ", Artem.height)
print("My height = ", Mark.height)

print("number of students =", Student.number)

print(Artem)
