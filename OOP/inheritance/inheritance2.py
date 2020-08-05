class Pet:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def show(self):
    print(f"I'm {self.name} and I'm {self.age} years old.")

  def speak(self):
    print('I dont know what to say.')

class Cat(Pet):
  def __init__(self, name, age, color):
    super().__init__(name, age)
    self.color = color

  def show(self):
    print(f"I'm {self.name}, {self.age} years old and I'm {self.color}.")

  def speak(self):
    print('Meow')

class Dog(Pet):
  def speak(self):
    print('Au au')



p1 = Pet('Luppy', 18)
c1 = Cat('July', 3, 'orange')
d1 = Dog('Beethoven', 1)

c1.show()