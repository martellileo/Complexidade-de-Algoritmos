#--- Top Down Memoization
def fibTD(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibTD(n - 1, memo) + fibTD(n - 2, memo)
    print(memo)
    return memo[n]

print(fibTD(6))

# Botton UP
def fibBU(n):
    dp = [0, 1]
    for i in range(2, n+1):
        dp.append(dp[i-1] + dp[i-2])
        print(dp)
    return dp[n]

print(fibBU(6))

# Mochila
def mochila(pesos, lucros, capacidade):
    n = len(pesos)
    V = [[0 for w in range(capacidade + 1)] for i in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacidade + 1):
            if pesos[i-1] > w:
                V[i][w] = V[i-1][w]
            else:
                V[i][w] = max(V[i-1][w], lucros[i-1] + V[i-1][w - pesos[i-1]])

    return V[n][capacidade], V

# Dados do problema
pesos = [1, 3, 5, 8]
lucros = [1, 5, 8, 10]
capacidade = 11

lucro_max, tabela = mochila(pesos, lucros, capacidade)
print("Lucro máximo:", lucro_max)

#--
def mochila_estudos(pesos, valores, capacidade):
    n = len(pesos)
    V = [[0 for w in range(capacidade + 1)] for i in range(n + 1)]

    # Preenchimento da tabela
    for i in range(1, n + 1):
        for w in range(1, capacidade + 1):
            if pesos[i-1] > w:
                V[i][w] = V[i-1][w]
            else:
                V[i][w] = max(V[i-1][w], valores[i-1] + V[i-1][w - pesos[i-1]])

    # Traceback para descobrir os itens escolhidos
    w = capacidade
    itens_escolhidos = []
    for i in range(n, 0, -1):
        if V[i][w] != V[i-1][w]:
            itens_escolhidos.append(i-1)  # item i foi incluído (índice i-1)
            w -= pesos[i-1]

    return V[n][capacidade], itens_escolhidos[::-1]  # inverter para ordem correta


# Dados
pesos = [3, 4, 2, 5, 1]
valores = [7, 9, 5, 10, 3]
capacidade = 10

lucro_max, itens = mochila_estudos(pesos, valores, capacidade)

# Resultado
print("Importância total máxima:", lucro_max)
print("Itens escolhidos (índice, peso, valor):")
for i in itens:
    print(f"Item {i+1} → peso: {pesos[i]}h, importância: {valores[i]}")

