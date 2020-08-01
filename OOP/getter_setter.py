class Dog:

  def __init__(self, name, age):
    self._name = name
    self._age = age

  def get_name(self):
    return self._name
  
  def get_age(self):
    return self._age
  
  def set_name(self, name):
    if isinstance(name, str):
      self._name = name
    else:
      print('O nome deve ser uma string')

  def set_age(self, age):
    if isinstance(age, int) and age >= 0:
      self._age = age
    else:
      print('Entre com uma idade válida.')
      

  def bark(self):
    print('Woof woof')



d1 = Dog('Luppy', 3)

print(d1.get_name())
d1.set_name('Joe')
print(d1.get_name())

print(d1.get_age())
d1.set_age(1)
print(d1.get_age())
