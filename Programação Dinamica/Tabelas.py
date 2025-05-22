def tabela_lucro(itens, capacidade_max):
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
    
    return dp

def tabela_binaria(itens, dp, capacidade_max):
    n = len(itens)
    binaria = [[0] * (capacidade_max + 1) for _ in range(n)]

    for i in range(n):
        peso_i, valor_i = itens[i]
        for w in range(1, capacidade_max + 1):
            if peso_i > w:
                binaria[i][w] = 0
            else:
                sem_item = dp[i-1][w] if i > 0 else 0
                com_item = valor_i + (dp[i-1][w - peso_i] if i > 0 else 0)
                binaria[i][w] = 1 if com_item > sem_item else 0
    
    return binaria

def imprimir_tabela(tabela, itens, titulo):
    print(titulo)
    print(" Peso →   ", end=" ")
    for w in range(1, len(tabela[0])):
        print(f"{w:3}", end=" ")
    print()
    for i in range(len(itens)):
        peso, valor = itens[i]
        print(f"{peso:2}kg {valor:3} |", end=" ")
        for w in range(1, len(tabela[0])):
            print(f"{tabela[i][w]:3}", end=" ")
        print()
    print()

# -----------------------------
# Joana
print("-----------")
print("Joana")
itens = [(1,3), (2,5), (4,9), (3,7)]
capacidade = 10
dp = tabela_lucro(itens, capacidade)
binaria = tabela_binaria(itens, dp, capacidade)
imprimir_tabela(dp, itens, "Tabela de Lucros:")
imprimir_tabela(binaria, itens, "Tabela Binária:")
print("-----------")

# Empresa
print("Empresa")
itens = [(6, 60), (4, 40), (5,50), (3, 30), (7, 70)]
capacidade = 10
dp = tabela_lucro(itens, capacidade)
binaria = tabela_binaria(itens, dp, capacidade)
imprimir_tabela(dp, itens, "Tabela de Lucros:")
imprimir_tabela(binaria, itens, "Tabela Binária:")
print("-----------")

# Pedro
print("Pedro")
itens = [(8,10), (5,7), (3,5), (2,4)]
capacidade = 10
dp = tabela_lucro(itens, capacidade)
binaria = tabela_binaria(itens, dp, capacidade)
imprimir_tabela(dp, itens, "Tabela de Lucros:")
imprimir_tabela(binaria, itens, "Tabela Binária:")
print("-----------")


