def busca():
    print("\nBusca")
    vetor = input("Digite os elementos separados por espaço ou digite 'aleatorio': ").strip()
    if vetor == 'aleatorio':
        import random
        vetor = [random.randint(0, 100) for _ in range(10)]
    else:
        vetor = list(map(int, vetor.split()))

    elemento = int(input("Elemento a ser buscado: "))

    print(  "\n[1] Busca Linear\n"
            "[2] Busca Binária\n"
            "[0] Voltar")
    metodo = input("Escolha o método: ").strip()

    if metodo == '1':
        for i, val in enumerate(vetor):
            if val == elemento:
                print(f"Elemento encontrado na posição {i}")
                return
        print("Elemento não encontrado")
    elif metodo == '2':
        vetor.sort()
        print("Vetor ordenado para busca binária:", vetor)
        esq, dir = 0, len(vetor) - 1
        while esq <= dir:
            meio = (esq + dir) // 2
            if vetor[meio] == elemento:
                print(f"Elemento encontrado na posição {meio}")
                return
            elif vetor[meio] < elemento:
                esq = meio + 1
            else:
                dir = meio - 1
        print("Elemento não encontrado")
    elif metodo == '0':
        return
    else:
        print("Método inválido")