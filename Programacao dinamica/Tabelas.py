def mochila_com_tabela(itens, capacidade_max):
    n = len(itens)
    dp = [[0] * (capacidade_max + 1) for _ in range(n)]

    for i in range(n):
        peso_i, valor_i = itens[i]
        for w in range(1, capacidade_max + 1):
            if peso_i > w:
                dp[i][w] = dp[i-1][w] if i > 0 else 0
            else:
                sem_item = dp[i-1][w] if i > 0 else 0
                com_item = valor_i + (dp[i-1][w - peso_i] if i > 0 else 0)
                dp[i][w] = max(sem_item, com_item)

    print("Tabela de Lucros:")
    print("Peso →   ", end=" ")
    for w in range(1, capacidade_max + 1):
        print(f"{w:3}", end=" ")
    print()
    for i in range(n):
        peso, valor = itens[i]
        print(f"{peso}kg {valor:3} |", end=" ")
        for w in range(1, capacidade_max + 1):
            print(f"{dp[i][w]:3}", end=" ")
        print()

    return dp

# Exercicios tabela
print("Joana")
itens = [(1,3), (2,5), (4,9), (3,7)]
capacidade = 10
mochila_com_tabela(itens, capacidade)
print("-----------")

print("Empresa")
itens = [(6, 60), (4, 40), (5,50), (3, 30), (7, 70)]
capacidade = 10
mochila_com_tabela(itens, capacidade)
print("-----------")

print("Pedro")
itens = [(8,10), (5,7), (3,5), (2,4)]
capacidade = 10
mochila_com_tabela(itens, capacidade)