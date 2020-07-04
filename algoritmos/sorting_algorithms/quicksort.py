"""Algoritmo para ordernar uma array do menor para o maior usando recursividade"""


def quicksort(arr):
    if len(arr) < 2:
        return arr     # caso-base
    else:
        pivo = arr[0]  # caso recursivo
        menores = [i for i in arr[1:] if i <= pivo]
        maiores = [i for i in arr[1:] if i > pivo]
        return quicksort(menores) + [pivo] + quicksort(maiores)


arr = [7, 6, 3, 10, 5, 2, 3]

print(quicksort(arr))


""" 'menores' desconstruido """
# for i in arr[1:]:
#     if i <= pivo:
#         menores.append(i)

""" 'maiores' desconstruido """
# for i in arr[1:]:
#     if i > pivo:
#         maiores.append(i)
