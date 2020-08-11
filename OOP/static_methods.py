# Static methods dont have access to instances of a class (objects). They do something, but they
# dont change anything. It is present in a class because it makes sense for the method to be present in class.

# They also CANNOT modify object instance state

# Unlike class methods, a static method does not need an implicit first argument (cls or self).


class Math:
  
  @staticmethod
  def add5(x):
    return x + 5

  @staticmethod
  def run():
    print('running...')

print(Math.add5(2))
Math.run()
