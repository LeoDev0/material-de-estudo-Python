"""Calculando fatorial usando recursão"""

def fat(n):
    if n == 1:
        return 1 
    else:
        return n * fat(n-1) # chamada recursiva 


"""nesse exemplo, a pilha (call stack) possui 3 chamadas:
a primeira fat(1) retorna 1
a segunda fat(2) retorna 2
a terceira fat(3) retorna 6"""
print(fat(3))
