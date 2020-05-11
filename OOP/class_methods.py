# Class methods don't need objects to be instanciated when used. A class method 
# is a method which is bound to the class and not the object of the class.

# They have the access to the state of the class as it takes a class parameter 
# that points to the class and not the object instance.

# It can modify a class state that would apply across all the instances of the class. 
# For example it can modify a class variable that will be applicable to all the instances. 


class Person:
  number_of_people = 0
  GRAVITY = -9.8

  def __init__(self, name):
    self.name = name
    Person.add_person()

  @classmethod
  def get_number_of_people(cls):
    return cls.number_of_people

  @classmethod
  def add_person(cls):
    cls.number_of_people += 1

print(Person.get_number_of_people())
p1 = Person('Gérson')
print(Person.get_number_of_people())