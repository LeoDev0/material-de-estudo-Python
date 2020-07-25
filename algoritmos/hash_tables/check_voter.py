"""
Código para demonstração/exemplificação da implementação 
interna do próprio python para hash tables.

Hash tables são uteis para pesquisa com tempo de execução
médio de O(1) para inserção, procura e remoção, ou seja,
extremamente rápidas.
"""


votaram = {'leo': True, 'maria': False}


def verifica_voto(eleitor):
    if votaram.get(eleitor):
        print('Já votou, mandei embora!')
    else:
        votaram[eleitor] = True
        print('Deixe votar')

verifica_voto('leo')
verifica_voto('maria')
verifica_voto('marco')

print(votaram)
