# Create a student Class
# that has a method `add_grade`, that takes a grade from 1 to 5
# an other method `get_average`, that returns the average of the
# grades

class Student(object):
    grades =[]

    def __init__(self):
        pass

    def add_grade(self,grade):
        if grade >= 1 and grade <= 5:
            self.grades.append(grade)
        else:
            print('Nana!')

    def get_average(self):
        return sum(self.grades) / len(self.grades)


pistike = Student()
pistike.add_grade(5)
pistike.add_grade(5)
pistike.add_grade(1)
pistike.add_grade(4)
pistike.add_grade(6)
pistike.add_grade(1)
print(pistike.get_average())