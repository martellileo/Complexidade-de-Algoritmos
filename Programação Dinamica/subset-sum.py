def subset_sum(n, T, numeros):
    # Adiciona zero no início para alinhar os índices
    numeros = [0] + numeros

    # Cria tabela booleana dp[i][t] = True se é possível formar soma t com os primeiros i elementos
    dp = [[False for _ in range(T + 1)] for _ in range(n + 1)]
    escolha = [[0 for _ in range(T + 1)] for _ in range(n + 1)]

    # Caso base: soma 0 é sempre possível (com subconjunto vazio)
    for i in range(n + 1):
        dp[i][0] = True

    for i in range(1, n + 1):
        for t in range(T + 1):
            if numeros[i] > t:
                dp[i][t] = dp[i - 1][t]
            else:
                sem_item = dp[i - 1][t]
                com_item = dp[i - 1][t - numeros[i]]
                dp[i][t] = sem_item or com_item
                if com_item:
                    escolha[i][t] = 1

    # Impressão da tabela de decisão (opcional)
    print("Tabela Booleana dp (True se soma possível):")
    for i in range(n + 1):
        print(f"{i:2d}: ", ["T" if dp[i][t] else "F" for t in range(T + 1)])

    # Reconstrução do subconjunto escolhido (se existir)
    if dp[n][T]:
        print("\nÉ possível formar a soma:", T)
        subconjunto = []
        i, t = n, T
        while t > 0 and i > 0:
            if escolha[i][t]:
                subconjunto.append(numeros[i])
                t -= numeros[i]
            i -= 1
        print("Subconjunto:", list(reversed(subconjunto)))
    else:
        print("\nNão é possível formar a soma:", T)

    return ""

# Exemplo de uso:
print(subset_sum(5, 10, [1,3,8, 4, 5]))
