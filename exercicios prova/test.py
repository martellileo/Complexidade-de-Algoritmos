print("---------------------------------------------------------")
#código ineficiente
#o(n2)

def encontrar_maior_ineficiente(lista):
    for i in range(len(lista)):
        maior = True
        for j in range(len(lista)):
            if lista[j] > lista[i]:
                maior = False
                break
        if maior:
            return lista[i]
        
def encontrar_maior_eficiente(lista):
    maior = lista[0]
    for i in lista:
        if i > maior:
            maior = i
    return maior

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 1]

inf = encontrar_maior_ineficiente(lista)
ef = encontrar_maior_eficiente(lista)
print("Ineficiente: ", inf)
print("Eficiente: ", ef)

print("---------------------------------------------------------")

# Código ineficiente
def encontrar_ordem_ineficiente(a, b, c):
    numeros = [a, b, c]
    for i in range(len(numeros)):
        maior = True
        for j in range(len(numeros)):
            if numeros[j] > numeros[i]:
                maior = False
                break
        if maior:
            maior_num = numeros[i]
    for i in range(len(numeros)):
        menor = True
        for j in range(len(numeros)):
            if numeros[j] < numeros[i]:
                menor = False
                break
        if menor:
            menor_num = numeros[i]

    meio_num = sum(numeros) - maior_num - menor_num
    return maior_num, meio_num, menor_num

def encontrar_ordem_eficiente(a, b, c):
    if a > b and a > c:
        maior = a
        meio, menor = b, c
        if c > b:
            meio, menor = c, b
    elif b > a and b > c:
        maior = b
        meio, menor = a, c
        if c > a:
            meio, menor = c, a
    else:
        maior = c
        meio, menor = a, b
        if b > a:
            meio, menor = b, a
    return maior, meio, menor

# def encontrar_ordem_eficiente(a, b, c):
#     if a > b and a > c:
#         maior = a
#         meio, menor = (b, c) if b > c else (c, b)
#     elif b > a and b > c:
#         maior = b
#         meio, menor = (a, c) if a > c else (c, a)
#     else:
#         maior = c
#         meio, menor = (a, b) if a > b else (b, a)
    
#     return maior, meio, menor


a, b, c = 3, 1, 4
maior, meio, menor = encontrar_ordem_ineficiente(a, b, c)
maiorEf, meioEf, menorEf = encontrar_ordem_eficiente(a, b, c)
print("Ineficiente -> Maior:", maior, "Meio:", meio, "Menor:", menor)
print("Eficiente -> Maior:", maiorEf, "Meio:", meioEf, "Menor:", menorEf)

print("---------------------------------------------------------")

# Exemplo 1: Encontrar o número que mais se repete em uma lista
# Código ineficiente
def mais_frequente_ineficiente(lista):
    max_contagem = 0
    mais_frequente = None
    for i in lista:
        contagem = 0
        for j in lista:
            if i == j:
                contagem += 1
        if contagem > max_contagem:
            max_contagem = contagem
            mais_frequente = i
    return mais_frequente

def mais_frequente_otimizado(lista):
    contagem = {}

    for item in lista:
        if item in contagem:
            contagem[item] += 1
        else:
            contagem[item] = 1

    # mais_frequente = None
    # max_contagem = 0
    # for item, count in contagem.items():
    #     if count > max_contagem:
    #         max_contagem = count
    #         mais_frequente = item
    # return mais_frequente

    contagem = sorted(contagem.items(), reverse=True, key=lambda item: item[1])
    return contagem[0][0]


lista_numeros = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print("Mais frequente (ineficiente):", mais_frequente_ineficiente(lista_numeros))
print("Mais frequente (otimizado):", mais_frequente_otimizado(lista_numeros))

print("---------------------------------------------------------")

def encontrar_pares_ineficientes(lista, alvo):
    pares = []
    for i in range (len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] + lista[j] == alvo:
                pares.append((lista[i], lista[j]))
    return pares