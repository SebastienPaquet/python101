class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)




studentA = Student("Quagmire",(80,70,90,94,86))
studentB = Student("Peter",(60,70,50,64,66))

print(studentA.name)
print(studentA.grades)
print(studentA.average_grade())

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"{self.name}, {self.age} ans"
    
    def __repr__(self) -> str:
        return f"<Person('{self.name}', {self.age})>"
    
bob = Person("Bob",33)
print(bob)
