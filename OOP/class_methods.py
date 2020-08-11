# Class methods don't need objects to be instanciated when used. A class method 
# is a method which is bound to the class and not the object of the class.

# They have the access to the state of the class as it takes a class parameter 
# that points to the class and not the object instance.

# It CAN modify a class state that would apply across all the instances of the class. 
# For example it can modify a class variable that will be applicable to all the instances. 

# It CANNOT modify object instance state

class Person:
  number_of_people = 0   # <-- Class Attribute: 
  GRAVITY = -9.8         # É um atributo DA CLASSE, e não da instância. São variáveis de 
                         # valor pré-definido de dentro da classe mas fora do método construtor
                         # (__init__), ou seja, todas as instâncias terão o valor padrão. 
                         # Não usa self e vc não precisa instanciar uma classe para acessar 
                         # um atributo de classe usando NomeDaClasse.nome_da_class_attribute.

  def __init__(self, name):
    self.name = name        # <--- Instance Attribute:
    Person.add_person()     # Variáveis definidas dentro do métodos construtor da classe, 
                            # ou seja, o valor é definido no momento da instanciação. Usa o self.	 

  @classmethod
  def get_number_of_people(cls):
    return cls.number_of_people

  @classmethod
  def add_person(cls):
    cls.number_of_people += 1

print(Person.get_number_of_people())
p1 = Person('Gérson')
print(Person.get_number_of_people())
