# Write a Person class that have a name and a birth_date property
# It should raise an error of the birthdate is less than 0 or more than 2016

class CTError(Exception):
    pass

class Person:

    def __init__(self, name, birth_date):
        self.name = name
        self.birth_date = birth_date
        self.birth_date_check()

    def birth_date_check(self):
        if self.birth_date < 0 or self.birth_date >= 2016:
            raise CTError("Kézműves error")

"""try:
    béla = Person('Béla', 2020)
except CTError:
    pass
"""