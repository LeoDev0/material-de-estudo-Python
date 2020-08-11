# https://realpython.com/python-kwargs-and-args/

"""
Args permite passar vários argumentos que se organizam
dentro de 'args' em forma de tupla (arg1, arg2, arg3)
"""
def my_sum(*args):
    result = 0
    for arg in args:
        result += arg
    print(result)

my_sum(1, 3, 4)

"""
Assim como o args, o kwargs permite entrar com 
vários argumentos, mas dessa vez em forma de chave=valor,
como como numa notação de objeto/dicionário
"""
def concatenate(**kwargs):
    result = ""
    for arg in kwargs.values():
        result += arg
    print(result)

concatenate(a='Python', b='Is', c='Great')


"""
The correct order for your parameters is:

    1. Standard arguments
    2. *args arguments
    3. **kwargs arguments


def my_function(a, b, *args, **kwargs):
    pass
"""
