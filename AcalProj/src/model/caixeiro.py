import itertools
import math
from itertools import combinations



def forca_bruta_tsp(cidades: list[tuple[float, float]]) -> tuple[float, list[int]]:
    n = len(cidades)
    indices = list(range(n))
    melhor_rota = []
    menor_custo = float('inf')

    for perm in itertools.permutations(indices[1:]):  # fixa a cidade 0
        rota = [0] + list(perm) + [0]
        custo = sum(
            distancia(cidades[rota[i]], cidades[rota[i + 1]])
            for i in range(n)
        )
        if custo < menor_custo:
            menor_custo = custo
            melhor_rota = rota

    return menor_custo, melhor_rota


# tupla de coordenadas (x, y), como [(0, 0), (1, 1), (2, 2)]
def distancia(p1: tuple[float, float], p2: tuple[float, float]) -> float:
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])


# retorna uma tupla (caminho, custo_total), como ([0, 1, 2, 0], 5.0)
def nearest_neighbor(cidades: list[tuple[float, float]]) -> tuple[list[int], float]:
    n = len(cidades)
    visitado = [False] * n
    caminho = [0]
    visitado[0] = True
    custo_total = 0

    for _ in range(n - 1):
        atual = caminho[-1]
        proxima = None
        menor_dist = float('inf')

        for i in range(n):
            if not visitado[i]:
                d = distancia(cidades[atual], cidades[i])
                if d < menor_dist:
                    menor_dist = d
                    proxima = i

        caminho.append(proxima)
        visitado[proxima] = True
        custo_total += menor_dist

    # voltar ao início
    custo_total += distancia(cidades[caminho[-1]], cidades[caminho[0]])
    caminho.append(0)

    return caminho, custo_total

# retorna uma tupla (custo_total, caminho), como (5.0, [0, 1, 2, 0])
def held_karp(cidades: list[tuple[float, float]]) -> tuple[float, list[int]]:
    n = len(cidades)
    dist = [[distancia(cidades[i], cidades[j]) for j in range(n)] for i in range(n)]

    # dp[mascara][i] = menor custo para chegar no subconjunto 'mascara' terminando na cidade 'i'
    dp = {}
    caminho = {}

    for k in range(1, n):
        dp[(1 << k, k)] = dist[0][k]

    for tamanho in range(2, n):
        for subconj in combinations(range(1, n), tamanho):
            bits = 0
            for bit in subconj:
                bits |= 1 << bit
            for k in subconj:
                prev_bits = bits & ~(1 << k)
                valores = [
                    (dp[(prev_bits, m)] + dist[m][k], m)
                    for m in subconj if m != k
                ]
                dp[(bits, k)], caminho[(bits, k)] = min(valores)

    bits_finais = (1 << n) - 2  # todas as cidades menos a 0
    valores_finais = [(dp[(bits_finais, k)] + dist[k][0], k) for k in range(1, n)]
    custo_total, ultimo = min(valores_finais)

    # reconstrução do caminho
    caminho_final = [0]
    bits = bits_finais
    atual = ultimo
    for _ in range(n - 1):
        caminho_final.append(atual)
        bits_antigo = bits
        bits &= ~(1 << atual)
        atual = caminho[(bits_antigo, atual)]
    caminho_final.append(0)
    caminho_final.reverse()

    return custo_total, caminho_final


def calcula_custo(caminho: list[int], cidades: list[tuple[float, float]]) -> float:
    return sum(distancia(cidades[caminho[i]], cidades[caminho[i + 1]]) for i in range(len(caminho) - 1))

# retorna uma tupla (caminho_otimizado, custo_otimizado), como ([0, 1, 2, 0], 5.0)
def two_opt(caminho: list[int], cidades: list[tuple[float, float]]) -> tuple[list[int], float]:
    melhor = caminho[:]
    melhor_custo = calcula_custo(melhor, cidades)
    melhorou = True

    while melhorou:
        melhorou = False
        for i in range(1, len(melhor) - 2):
            for j in range(i + 1, len(melhor) - 1):
                if j - i == 1:  # não faz sentido inverter segmentos adjacentes
                    continue
                novo = melhor[:]
                novo[i:j] = reversed(melhor[i:j])
                novo_custo = calcula_custo(novo, cidades)
                if novo_custo < melhor_custo:
                    melhor = novo
                    melhor_custo = novo_custo
                    melhorou = True
        # sai do loop se nenhuma melhoria foi feita

    return melhor, melhor_custo






