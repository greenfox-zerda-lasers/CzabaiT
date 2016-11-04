# Create a new class called `Person` that has a first_name and a last_name (takes it in it's constructor)
# It should have a `greet` method that prints it's full name

# Create a `Student` class that is the child class of `Person`
# it should have a method to add grades
# it should have a `salute` method that prints it's full name and the average of it's grades as well

class Person(object):

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def greet(self):
        return 'Heyho ' + self.first_name + ' ' + self.last_name + '!'

class Student(Person):
    grades = []

    def add_grade(self,grade):
        self.grades.append(grade)

    def salute(self):
        print(self.greet(),sum(self.grades) / len(self.grades))

pistike = Student('Pisti', 'Lókötő')

pistike.greet()
pistike.add_grade(5)
pistike.add_grade(4)
pistike.add_grade(4)
pistike.salute()
