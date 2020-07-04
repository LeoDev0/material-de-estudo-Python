"""Algoritmo para ordernar uma array do menor para o maior"""


def busca_menor(arr):
    menor = arr[0]
    menor_indice = 0
    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i
    return menor_indice


def ordenacao_por_selecao(arr):
    novo_arr = []
    for i in range(len(arr)):
        # Encontra o menor elemento no array e adiciona no novo array
        menor = busca_menor(arr)
        novo_arr.append(arr.pop(menor))
    return novo_arr


arr = [3, 7, 5, 0, 2, 1]

print(ordenacao_por_selecao(arr))
