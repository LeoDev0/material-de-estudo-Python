import sys


"""
Diferentemente de listas, generators não armazenam cada
iteração dentro de uma lista, apenas o último valor, o que
economiza espaço na memória e aumenta performance na execução
da tarefa.
"""
lista = [i for i in range(1, 1000)]
generator = (i for i in range(1, 1000))


print(sys.getsizeof(lista)) # 9032 bytes
print(sys.getsizeof(generator)) # 128 bytes
print(sum(generator)) 
print(sum(lista))


"""Generators fora de list comprehension usam o 'yield'"""
# def range_generator(start, stop):
#     for i in range(start, stop + 1):
#         yield i

# generator = range_generator(1, 1000)

# def range_lista(start, stop):
#     result = []
#     for i in range(start, stop + 1):
#         lista.append(i)
#     return result

# lista = range_lista(1, 1000)


# print(sys.getsizeof(lista))
# print(sys.getsizeof(generator))
# print(sum(lista))
# print(sum(generator))
