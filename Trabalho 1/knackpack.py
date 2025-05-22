def knapsack(pesos, valores, capacidade):
    n = len(pesos)
    dp = [[0] * (capacidade + 1) for _ in range(n + 1)]
    binaria = [[0] * (capacidade + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        peso = pesos[i-1]
        valor = valores[i-1]
        for w in range(1, capacidade + 1):
            if peso > w:
                dp[i][w] = dp[i-1][w]
                binaria[i][w] = 0
            else:
                sem_item = dp[i-1][w]
                com_item = valor + dp[i-1][w - peso]
                if com_item > sem_item:
                    dp[i][w] = com_item
                    binaria[i][w] = 1
                else:
                    dp[i][w] = sem_item
                    binaria[i][w] = 0

    valor_maximo = dp[n][capacidade]

    w = capacidade
    itens_selecionados = []
    for i in range(n, 0, -1):
        if binaria[i][w] == 1:
            itens_selecionados.append(i-1)
            w -= pesos[i-1]

    itens_selecionados.reverse()

    print("Tabela de Valores (Lucros):")
    for i in range(n+1):
        for w in range(capacidade + 1):
            print(f"{dp[i][w]:4}", end=" ")
        print()

    print("\nTabela Binária:")
    for i in range(n+1):
        for w in range(capacidade + 1):
            print(f"{binaria[i][w]:4}", end=" ")
        print()

    print("\nValor máximo possível:", valor_maximo)
    print("Itens selecionados:", itens_selecionados)
    print("Detalhes dos itens selecionados:")
    for i in itens_selecionados:
        print(f" - Item {i}: Peso = {pesos[i]}, Valor = {valores[i]}")

pesos = [1, 2, 3, 4, 5]
valores = [10, 20, 30, 40, 50]
capacidade = 10

knapsack(pesos, valores, capacidade)
