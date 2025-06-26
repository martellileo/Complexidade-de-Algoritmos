import itertools
import math
import random
import time

def distancia(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def gerar_matriz(cidades):
    n = len(cidades)
    matriz = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                matriz[i][j] = distancia(cidades[i], cidades[j])
    return matriz

def tsp_brute_force(matriz):
    n = len(matriz)
    perm = itertools.permutations(range(n))
    melhor_caminho = None
    menor_custo = float('inf')
    for p in perm:
        custo = sum(matriz[p[i]][p[i+1]] for i in range(n-1)) + matriz[p[-1]][p[0]]
        if custo < menor_custo:
            menor_custo = custo
            melhor_caminho = p
    return melhor_caminho, menor_custo

def tsp_nearest_neighbor(matriz):
    n = len(matriz)
    visitado = [False] * n
    caminho = [0]
    visitado[0] = True
    atual = 0
    for _ in range(n - 1):
        proximo = min([(i, matriz[atual][i]) for i in range(n) if not visitado[i]], key=lambda x: x[1])[0]
        caminho.append(proximo)
        visitado[proximo] = True
        atual = proximo
    return caminho, sum(matriz[caminho[i]][caminho[i+1]] for i in range(n-1)) + matriz[caminho[-1]][caminho[0]]

def tsp_2opt(caminho, matriz):
    def custo(c):
        return sum(matriz[c[i]][c[i+1]] for i in range(len(c)-1)) + matriz[c[-1]][c[0]]

    n = len(caminho)
    melhor = caminho[:]
    melhor_custo = custo(melhor)
    melhorou = True
    while melhorou:
        melhorou = False
        for i in range(1, n - 2):
            for j in range(i + 1, n):
                if j - i == 1: continue
                novo = melhor[:]
                novo[i:j] = reversed(novo[i:j])
                novo_custo = custo(novo)
                if novo_custo < melhor_custo:
                    melhor = novo[:]
                    melhor_custo = novo_custo
                    melhorou = True
    return melhor, melhor_custo

def caixeiro_viajante():
    print("\nCaixeiro Viajante")
    n = int(input("Quantidade de cidades: "))
    tipo = input("Inserir coordenadas manualmente (s/n)? ").strip().lower()

    if tipo == 's':
        cidades = []
        for i in range(n):
            x = float(input(f"Cidade {i} - x: "))
            y = float(input(f"Cidade {i} - y: "))
            cidades.append((x, y))
    else:
        cidades = [(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(n)]

    matriz = gerar_matriz(cidades)

    print(  "\n[1] Força Bruta (n pequeno)" \
            "\n[2] Nearest Neighbor (heurístico)\n"
            "[3] 2-opt (refinamento do vizinho mais próximo)")
    metodo = input("Escolha o método: ").strip()

    inicio = time.time()
    if metodo == '1':
        caminho, custo_total = tsp_brute_force(matriz)
    elif metodo == '2':
        caminho, custo_total = tsp_nearest_neighbor(matriz)
    elif metodo == '3':
        base, _ = tsp_nearest_neighbor(matriz)
        caminho, custo_total = tsp_2opt(base, matriz)
    else:
        print("Método inválido")
        return
    fim = time.time()

    print("\nOrdem das cidades:", caminho)
    print("Custo total do caminho:", round(custo_total, 2))
    print("Tempo de execução:", round(fim - inicio, 4), "s")