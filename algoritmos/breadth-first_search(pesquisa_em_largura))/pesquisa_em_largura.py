"""
O Breadth-first Search, ou Pesquisa em Largura, é o algoritmo que resolve 
problemas de caminho mínimo entre dois pontos.

Esse algoritmo utiliza um modelo de grafos, que são um conjunto de
conexões formados por vértices (círculos) e arestas (setas) que 
representam eventos diferentes conectados entre si.

A pesquisa em largura usa filas (FIFO) em detrimento de pilhas (LIFO)
na execução de cada verificação.

O exemplo abaixo pesquisa na rede de contatos de uma pessoa se alguém
é vendedor de manga.
"""

from collections import deque


grafo = {}
grafo["you"] = ["alice", "bob", "claire"]
grafo["bob"] = ["anuj", "peggy"]
grafo["alice"] = ["peggy"]
grafo["claire"] = ["thom", "jonny"]
grafo["anuj"] = []
grafo["peggy"] = []
grafo["thom"] = []
grafo["jonny"] = []

# Critério para definir se uma pessoa é vendedora de manga
def pessoa_eh_vendedora(nome):
    return nome[-1] == 'm'
    # sufixo = nome[-3] + nome[-2] + nome[-1]
    # return sufixo == ' -v'

def pesquisa(nome):
    fila_de_pesquisa = deque()
    fila_de_pesquisa += grafo[nome]
    verificadas = []  # Sem verificação de nomes já pesquisados, esse algoritmo pode falhar ao cair num loop infinito
    while fila_de_pesquisa:
        pessoa = fila_de_pesquisa.popleft()
        if not pessoa in verificadas:
            if pessoa_eh_vendedora(pessoa):
                print(f'{pessoa} é um vendedor de manga!')
                return True
            else:
                fila_de_pesquisa += grafo[pessoa]
                verificadas.append(pessoa)
    print('Não há nenhum vendedor de manga nos contatos.')
    return False

pesquisa('you')


"""
OBS 1: Existe um tipo especial de grafo chamado árvore em que nenhuma
aresta (seta) aponta de volta, mas sempre para baixo, como é uma
árvore genealógica. Neste tipo de grafo, todas as arestas apontam
para baixo, pois não faria sentido uma árvore genealógica ter arestas
apontando para cima, pois seu pai não pode ser o pai do seu avô.

OBS 2: Um grafo que contém setas e relações seguindo a direção das 
setas é chamada Dígrafo. Nos Dígrafos a relação acontece apenas em
um sentido, os vértices são vizinhos um do outro. 
"""