def otimizacao():
    print("\nOtimização")
    print("[1] Mochila 0-1")
    print("[2] Mochila Fracionária")
    print("[3] Corte de Barras (Rod Cutting)")
    print("[4] Coin Change (Troco Mínimo)")
    print("[0] Voltar")
    escolha = input("Opção: ")

    if escolha == '1':
        mochila_01()
    elif escolha == '2':
        mochila_fracionaria()
    elif escolha == '3':
        corte_barras()
    elif escolha == '4':
        coin_change()
    elif escolha == '0':
        return
    else:
        print("Opção inválida.")

def mochila_01():
    print("\n--- Mochila 0-1 (Programação Dinâmica) ---")
    pesos = list(map(int, input("Pesos dos itens: ").split()))
    valores = list(map(int, input("Valores dos itens: ").split()))
    capacidade = int(input("Capacidade da mochila: "))

    n = len(pesos)
    dp = [[0 for _ in range(capacidade + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacidade + 1):
            if pesos[i - 1] <= w:
                dp[i][w] = max(valores[i - 1] + dp[i - 1][w - pesos[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    print("Valor ótimo:", dp[n][capacidade])
    print("Tabela:")
    for linha in dp:
        print(linha)


def mochila_fracionaria():
    print("\n--- Mochila Fracionária (Guloso) ---")
    n = int(input("Quantidade de itens: "))
    itens = []
    for i in range(n):
        v = int(input(f"Valor do item {i+1}: "))
        p = int(input(f"Peso do item {i+1}: "))
        itens.append((v / p, v, p))

    capacidade = int(input("Capacidade da mochila: "))
    itens.sort(reverse=True)

    total = 0
    for frac, val, pes in itens:
        if capacidade >= pes:
            capacidade -= pes
            total += val
        else:
            total += frac * capacidade
            break

    print("Valor total na mochila:", total)


def corte_barras():
    print("\n--- Corte de Barras (Rod Cutting) ---")
    preco = list(map(int, input("Valores por tamanho: ").split()))
    n = len(preco)
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        for j in range(i):
            dp[i] = max(dp[i], preco[j] + dp[i - j - 1])

    print("Valor máximo obtido:", dp[n])
    print("Tabela:", dp)


def coin_change():
    print("\n--- Coin Change (Troco Mínimo) ---")
    moedas = list(map(int, input("Valores das moedas: ").split()))
    valor = int(input("Valor a ser alcançado: "))

    dp = [float('inf')] * (valor + 1)
    dp[0] = 0

    for i in range(1, valor + 1):
        for moeda in moedas:
            if i - moeda >= 0:
                dp[i] = min(dp[i], dp[i - moeda] + 1)

    if dp[valor] == float('inf'):
        print("Não é possível formar o valor com as moedas fornecidas.")
    else:
        print("Número mínimo de moedas:", dp[valor])
        print("Tabela:", dp)