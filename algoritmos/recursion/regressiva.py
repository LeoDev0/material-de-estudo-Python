"""Contagem regressiva usando recursão"""

def regressiva(i):
    print(i)
    if i <= 1: # caso-base
        pass
    else:      # caso recursivo
        regressiva(i-1)


regressiva(10)
