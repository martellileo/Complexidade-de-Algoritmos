def mochila_fracionaria_tabela(pesos, valores, capacidade_max):
    n = len(pesos)
    itens = [(i, pesos[i], valores[i], valores[i]/pesos[i]) for i in range(n)]
    itens.sort(key=lambda x: x[3], reverse=True)

    tabela_valores = [[0.0] * (capacidade_max + 1) for _ in range(n)]
    tabela_frac = [[0.0] * (capacidade_max + 1) for _ in range(n)]

    for i, peso, valor, vp in itens:
        for c in range(capacidade_max + 1):
            if i == 0:
                if peso <= c:
                    tabela_valores[i][c] = valor
                    tabela_frac[i][c] = 1.0
                else:
                    frac = c / peso
                    tabela_valores[i][c] = valor * frac
                    tabela_frac[i][c] = frac
            else:
                if peso <= c:
                    valor_completo = valor + tabela_valores[i-1][c - peso]
                    if valor_completo > tabela_valores[i-1][c]:
                        tabela_valores[i][c] = valor_completo
                        tabela_frac[i][c] = 1.0
                    else:
                        tabela_valores[i][c] = tabela_valores[i-1][c]
                        tabela_frac[i][c] = 0.0
                else:
                    frac = c / peso
                    valor_fracionado = valor * frac + tabela_valores[i-1][0]
                    if valor_fracionado > tabela_valores[i-1][c]:
                        tabela_valores[i][c] = valor_fracionado
                        tabela_frac[i][c] = frac
                    else:
                        tabela_valores[i][c] = tabela_valores[i-1][c]
                        tabela_frac[i][c] = 0.0

    valor_maximo = tabela_valores[n-1][capacidade_max]

    c = capacidade_max
    fracoes_selecionadas = [0.0] * n
    for i in range(n-1, -1, -1):
        fracao = tabela_frac[i][c]
        fracoes_selecionadas[i] = fracao
        peso = itens[i][1]
        c -= int(peso * fracao)
        if c < 0:
            c = 0

    resultado_frações = [0.0] * n
    for idx, (i, peso, valor, vp) in enumerate(itens):
        resultado_frações[i] = fracoes_selecionadas[idx]

    print("Tabela de Valores:")
    print("Capacidade → ", end="")
    for c in range(capacidade_max + 1):
        print(f"{c:6}", end=" ")
    print()
    for i, (idx, peso, valor, vp) in enumerate(itens):
        print(f"Item {idx} ({peso}kg): ", end="")
        for c in range(capacidade_max + 1):
            print(f"{tabela_valores[i][c]:6.1f}", end=" ")
        print()

    print("\nTabela Binária:")
    print("Capacidade → ", end="")
    for c in range(capacidade_max + 1):
        print(f"{c:6}", end=" ")
    print()
    for i, (idx, peso, valor, vp) in enumerate(itens):
        print(f"Item {idx} ({peso}kg): ", end="")
        for c in range(capacidade_max + 1):
            print(f"{tabela_frac[i][c]:6.2f}", end=" ")
        print()

    print(f"\nValor máximo obtido: {valor_maximo:.2f}")
    print("Frações dos itens selecionados:")
    for i in range(n):
        if resultado_frações[i] > 0:
            print(f" - Item {i}: fração {resultado_frações[i]:.4f}, peso usado = {pesos[i] * resultado_frações[i]:.2f}, valor = {valores[i] * resultado_frações[i]:.2f}")

pesos = [1, 2, 3, 4, 5]
valores = [10, 20, 30, 40, 50]
capacidade = 10

mochila_fracionaria_tabela(pesos, valores, capacidade)
