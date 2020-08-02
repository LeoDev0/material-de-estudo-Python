# USING THE property() METHOD 
class Cat:

    def __init__(self, nome, idade):
        self._nome = nome
    
    def get_nome(self):
        return self._nome
    
    def set_nome(self, nome):
        if isinstance(nome, str):
            self._nome = nome
        else:
            print('O nome deve ser uma string')

    def del_nome(self):
        del self._nome

    nome = property(get_nome, set_nome, del_nome)
    
c = Cat('Luppy', 15)

print(c.nome)
c.nome = 'leo'
print(c.nome)
del c.nome
print(c.nome)




# USING THE @property DECORATOR (recommended)
class Dog:

    def __init__(self, breed):
        self._breed = breed

    @property
    def breed(self):
        return self._breed
    
    @breed.setter
    def breed(self, breed):
        if isinstance(breed, str):
            self._breed = breed
        else:
            print('A raça deve ser uma string')
    
    @breed.deleter
    def breed(self):
        del self._breed


d = Dog('Labrador')

print(d.breed)
d.breed = 'Pitbull'
print(d.breed)
del d.breed
print(d.breed)
