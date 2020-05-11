class Dog:

  def __init__(self, name, age):
    self.name = name
    self.age = age

  def get_name(self):
    return self.name
  
  def get_age(self):
    return self.age
  
  def set_name(self, name):
    self.name = name

  def set_age(self, age):
    self.age = age

  def bark(self):
    print('Woof woof')



d1 = Dog('Luppy', 3)

print(d1.get_name())
d1.set_name('Joe')
print(d1.get_name())
