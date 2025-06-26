

def busca_linear(lista:list, valor:int):
    comparacoes = 0
    for i, item in enumerate(lista):
        comparacoes += 1
        if item == valor:
            return i, comparacoes
    return -1, comparacoes

def busca_binaria(lista:list, valor:int):
    comparacoes = 0
    esquerda, direita = 0, len(lista) - 1

    while esquerda <= direita:
        comparacoes += 1
        meio = (esquerda + direita) // 2
        if lista[meio] == valor:
            return meio, comparacoes
        elif lista[meio] < valor:
            esquerda = meio + 1
        else:
            direita = meio - 1

    return -1, comparacoes