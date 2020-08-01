# PUBLIC ATTRIBUTES: Pode ser acessado e modificado em qualquer lugar do programa.

# PROTECTED ATTRIBUTES: (_atributo) É um SINALIZAÇÃO aos desenvolvedores 
# de que o atributo só deve ser acessado dentro da própria classe. É 
# apenas uma sinalização porque na prática é possível acessá-lo de
# qualquer lugar no programa.   

# PRIVATE ATTRIBUTES: (__atributo) Acesso fora da classe limitado/dificultado
# Dificulta o acesso, mas não torna impossível. Útil para evitar 'name clashes'
# Para acessar: _NomeDaClasse__nome_do_atributo.
# O google style-guide recomenda só usar em casos especiais, pois não é a forma
# padrão de tornar um atributo privado (que seria o single-leading underscore)
# por tornar o código menos legível e dificulta na testagem do código.

# ABOUT Private Attributes: 
# - Adding two leading underscores (__) before the name of an attribute 
# will trigger a process called "name mangling" and an error will be
# thrown if you try to access the attribute directly.
# - Any identifier of the form __spam (at least two leading underscores,
# at most one trailing underscore) is textually replaced with _classname__spam,
# where classname is the current class name with leading underscore(s) stripped.


class Player:

    def __init__(self, username, rank, time_played):
        self.username = username  # Public attribute
        self._rank = rank  # Protected attribute
        self.__time_played = time_played  # Private attribute


player1 = Player('Mario', 1, 1000)

print(player1.username)  # Output: Mario
print(player1._rank)  # Output: 1
print(player1._Player__time_played)  # Output: 1000
print(player1.__time_played)  # Output: AttributeError
