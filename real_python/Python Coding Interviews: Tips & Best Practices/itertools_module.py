import itertools


friends = ['Monique', 'Ashish', 'Devon', 'Bernie']

"""
itertools.permutations monta uma lista com todas as permutações,
ou seja, lista com todas as combinações possíveis de agrupamentos
de itens na lista com o tamanho do grupo especificado (r=2)
"""
permutations = list(itertools.permutations(friends, r=2))
print(permutations)
# [('Monique', 'Ashish'), ('Monique', 'Devon'), ('Monique', 'Bernie'),
# ('Ashish', 'Monique'), ('Ashish', 'Devon'), ('Ashish', 'Bernie'),
# ('Devon', 'Monique'), ('Devon', 'Ashish'), ('Devon', 'Bernie'),
# ('Bernie', 'Monique'), ('Bernie', 'Ashish'), ('Bernie', 'Devon')]


"""
itertools.combinations monta uma lista de combinações, que também
agrupa itens de acordo com o tamanho especificado mas nesse caso
a ordem dos itens não importa, ou seja, não há combinações repetidas
e por consequência a lista é menor.
"""
combinations = list(itertools.combinations(friends, r=2))
print(combinations)
# [('Monique', 'Ashish'), ('Monique', 'Devon'), ('Monique', 'Bernie'),
# ('Ashish', 'Devon'), ('Ashish', 'Bernie'), ('Devon', 'Bernie')]


"""Repetir um elemento "times" vezes"""
all_ones = list(itertools.repeat(1, times=5))
print(all_ones)
# [1, 1, 1, 1, 1]


"""Pega um elemento iterável e repete ele infinitamente"""
alternating_ones = itertools.cycle([1, -1])
# next(alternating_ones)
# 1

# next(alternating_ones)
# -1
