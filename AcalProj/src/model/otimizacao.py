


# pesos = list[int], valores = list[int], capacidade = int. Retorna -> valor_total = int, itens_selecionados = list[int], tabela = list[list[int]]
def mochila_01(pesos:list, valores:list, capacidade:int):

    n = len(pesos)
    tabela = [[0 for _ in range(capacidade + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacidade + 1):
            if pesos[i - 1] <= w:
                tabela[i][w] = max(
                    valores[i - 1] + tabela[i - 1][w - pesos[i - 1]],
                    tabela[i - 1][w]
                )
            else:
                tabela[i][w] = tabela[i - 1][w]

    valor_total = tabela[n][capacidade]
    w = capacidade
    itens_selecionados = []

    for i in range(n, 0, -1):
        if tabela[i][w] != tabela[i - 1][w]:
            itens_selecionados.append(i - 1)
            w -= pesos[i - 1]

    itens_selecionados.reverse()
    return valor_total, itens_selecionados, tabela



# pesos = list[int ou float], valores = list[int ou float], capacidade = int. Retorna -> valor_total = float, itens = list[tuple(int, int)]
def mochila_fracionaria(pesos:list, valores:list, capacidade:int):
    n = len(pesos)
    razao = [(valores[i] / pesos[i], pesos[i], valores[i]) for i in range(n)]
    razao.sort(reverse=True)

    valor_total = 0
    itens = []

    for r, peso, valor in razao:
        if capacidade >= peso:
            capacidade -= peso
            valor_total += valor
            itens.append((peso, valor))
        else:
            frac = capacidade / peso
            valor_total += valor * frac
            itens.append((peso * frac, valor * frac))
            break

    return valor_total, itens


# pesos = list[int], precos = list[int], tamanho = int. Retorna -> valor_maximo = int, cortes = list[int]
# tupla de retorno: (valor_maximo, cortes)
def corte_de_barras(precos: list, tamanho: int) -> tuple[int, list]:
    dp = [0] * (tamanho + 1)
    cortes = [0] * (tamanho + 1)

    for i in range(1, tamanho + 1):
        max_valor = float('-inf')
        for j in range(1, i + 1):
            if j <= len(precos):
                if max_valor < precos[j - 1] + dp[i - j]:
                    max_valor = precos[j - 1] + dp[i - j]
                    cortes[i] = j
        dp[i] = max_valor

    # Recuperando os cortes feitos
    resultado_cortes = []
    k = tamanho
    while k > 0:
        resultado_cortes.append(cortes[k])
        k -= cortes[k]

    return dp[tamanho], resultado_cortes


# moedas = list[int], valor = int. Retorna -> (quantidade_minima, lista_de_moedas_usadas)
# tupla de retorno: (quantidade_minima, lista_de_moedas_usadas)
def troco_minimo(moedas: list, valor: int) -> tuple[int, list]:
    dp = [float('inf')] * (valor + 1)
    dp[0] = 0
    usadas = [-1] * (valor + 1)

    for i in range(1, valor + 1):
        for moeda in moedas:
            if moeda <= i and dp[i - moeda] + 1 < dp[i]:
                dp[i] = dp[i - moeda] + 1
                usadas[i] = moeda

    if dp[valor] == float('inf'):
        return -1, []  # Sem solução possível

    # Recuperando moedas usadas
    resultado = []
    k = valor
    while k > 0:
        resultado.append(usadas[k])
        k -= usadas[k]

    return int(dp[valor]), resultado



