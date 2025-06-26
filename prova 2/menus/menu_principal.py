def menu_principal():
    while True:
        print("\nAlgoritmos Clássicos")
        print("[1] Ordenação")
        print("[2] Busca")
        print("[3] Otimização")
        print("[4] Caixeiro Viajante")
        print("[0] Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == '1':
            from modulos.ordenacao import ordenacao
            ordenacao()
        elif opcao == '2':
            from modulos.busca import busca
            busca()
        elif opcao == '3':
            from modulos.otimizacao import otimizacao
            otimizacao()
        elif opcao == '4':
            from modulos.caixeiro import caixeiro_viajante
            caixeiro_viajante()
        elif opcao == '0':
            print("encerrando!")
            break
