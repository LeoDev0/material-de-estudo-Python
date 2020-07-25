"""
Código para demonstração fictícia da implementação de um sistema
de cache de páginas de um site usando hash tables. É comumente usado para economizar
requisições repetidas e desnecessários ao servidor.
"""

cache = dict()

def requisita_pagina(url):
    if cache.get(url):
        return cache[url]
    else:
        dados = pega_dados_do_servidor(url)
        cache[url] = dados
        return dados
