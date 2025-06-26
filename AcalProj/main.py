import random
import csv
import matplotlib.pyplot as plt
import time
import src.model.busca
import src.model.ordenacao
import src.model.otimizacao
import src.model.caixeiro
import src.model.extras
from src.model.ordenacao import bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort, heap_sort
from src.model.busca import busca_linear, busca_binaria
from src.model.otimizacao import mochila_01, mochila_fracionaria, corte_de_barras, troco_minimo
from src.model.caixeiro import forca_bruta_tsp, nearest_neighbor, held_karp, two_opt
from src.model.extras import salvar_instancia, carregar_instancia, exportar_resultado_csv, plot_comparativo

def gerar_lista(tamanho: int, ordenado=False, crescente=False, decrescente=False, quase_ordenado=False):
  lista = random.sample(range(tamanho), tamanho)

  if ordenado:
      if crescente:
          lista.sort()
      elif decrescente:
          lista.sort(reverse=True)
      elif quase_ordenado:
          lista.sort()
          if tamanho > 1:
              lista[0], lista[-1] = lista[-1], lista[0]

  return lista


def menu_ordenacao():
    print("==== MENU DE ORDENACAO ====")
    print("1 - Bubble Sort")
    print("2 - Selection Sort")
    print("3 - Insertion Sort")
    print("4 - Merge Sort")
    print("5 - Quick Sort")
    print("6 - Heap Sort")
    print("0 - Voltar ao menu principal")
    print("Escolha uma opcao: ", end="")
    escolha = input().strip()
    if escolha == '0':
        return
    elif escolha > '6' or escolha < '0':
        print("Opcao invalida. Tente novamente.")
        return menu_ordenacao()
    else:
        return escolha


def menu_busca():
    print("==== MENU DE BUSCA ====")
    print("1 - Busca Linear")
    print("2 - Busca Binaria")
    print("0 - Voltar ao menu principal")
    print("Escolha uma opcao: ", end="")
    escolha = input().strip()
    if escolha == '0':
        return
    elif escolha > '2' or escolha < '0':
        print("Opcao invalida. Tente novamente.")
        return menu_busca()
    else:
        return escolha


def menu_otimizacao():
    print("==== MENU DE OTIMIZACAO ====")
    print("1 - Mochila 01")
    print("2 - Mochila Fracionaria")
    print("3 - Corte de Barras")
    print("4 - Troco Minimo")
    print("0 - Voltar ao menu principal")
    print("Escolha uma opcao: ", end="")
    escolha = input().strip()
    if escolha == '0':
        return
    elif escolha > '4' or escolha < '0':
        print("Opcao invalida. Tente novamente.")
        return menu_otimizacao()
    else:
        return escolha


def menu_caixeiro():
    print("==== MENU DO CAIXEIRO VIAJANTE ====")
    print("1 - Forca Bruta")
    print("2 - Vizinho Mais Proximo")
    print("3 - Held-Karp")
    print("4 - two-opt")
    print("0 - Voltar ao menu principal")
    escolha = input("Escolha uma opcao: ").strip()
    if escolha == '0':
        return
    elif escolha > '4' or escolha < '0':
        print("Opcao invalida. Tente novamente.")
        return menu_caixeiro()
    else:
        return escolha


def menu_extras():
    print("==== MENU DE EXTRAS ====")
    print("1 - Salvar Instância de Cidades (TSP)")
    print("2 - Carregar Instância de Cidades (TSP)")
    print("3 - Exportar Resultado TSP para CSV")
    print("4 - Plot Comparativo de Métodos TSP")
    print("0 - Voltar ao menu principal")
    escolha = input("Escolha uma opcao: ").strip()
    if escolha == '0':
        return
    elif escolha > '4' or escolha < '0':
        print("Opcao invalida. Tente novamente.")
        return menu_extras()
    else:
        return escolha


def menu_principal():
    print("==== MENU PRINCIPAL ====")
    print("1 - Ordenacao")
    print("2 - Busca")
    print("3 - Otimizacao")
    print("4 - Caixeiro Viajante")
    print("5 - Extras")
    print("0 - Sair")
    escolha = input("Escolha uma opcao: ").strip()
    if escolha == '0':
        print("Saindo do programa...")
        return
    elif escolha > '5' or escolha < '0':
        print("Opcao invalida. Tente novamente.")
        return menu_principal()
    else:
        return escolha




def main():
    while True:
        opcao = menu_principal()
        if opcao == '0' or opcao is None:
            break
        elif opcao == '1':  # Ordenação
            escolha = menu_ordenacao()
            if escolha is None or escolha == '0':
                continue
            tamanho = int(input('Tamanho da lista: '))
            print("Opções de ordenação:")
            print("1 - Ordenado Crescente")
            print("2 - Ordenado Decrescente")
            print("3 - Quase Ordenado")
            print("4 - Aleatório")
            ordenacao = input("Escolha uma opção (1-4): ").strip()
            if ordenacao == '1':
                ordenado = True
                crescente = True
                decrescente = False
                quase_ordenado = False
            elif ordenacao == '2':
                ordenado = True
                crescente = False
                decrescente = True
                quase_ordenado = False
            elif ordenacao == '3':
                ordenado = True
                crescente = False
                decrescente = False
                quase_ordenado = True
            elif ordenacao == '4':
                ordenado = False
                crescente = False
                decrescente = False
                quase_ordenado = False
            else:
                print("Opção inválida. Usando lista aleatória.")
                ordenado = False
                crescente = False
                decrescente = False
                quase_ordenado = False
            lista = gerar_lista(tamanho, ordenado=ordenado, crescente=crescente, decrescente=decrescente, quase_ordenado=quase_ordenado)
            print('Lista original:', lista)
            mostrar_passos = input('Mostrar passos? (s/n): ').strip().lower() == 's'
            if escolha == '1':
                from src.model.ordenacao import bubble_sort
                resultado, tempo = bubble_sort(lista.copy(), tamanho, mostrar_passos)
                print('Resultado:', resultado, '\nTempo:', tempo)
            elif escolha == '2':
                from src.model.ordenacao import selection_sort
                resultado, tempo = selection_sort(lista.copy(), tamanho, mostrar_passos)
                print('Resultado:', resultado, '\nTempo:', tempo)
            elif escolha == '3':
                from src.model.ordenacao import insertion_sort
                resultado, tempo = insertion_sort(lista.copy(), tamanho, mostrar_passos)
                print('Resultado:', resultado, '\nTempo:', tempo)
            elif escolha == '4':
                from src.model.ordenacao import merge_sort
                resultado, tempo = merge_sort(lista.copy(), tamanho, mostrar_passos)
                print('Resultado:', resultado, '\nTempo:', tempo)
            elif escolha == '5':
                from src.model.ordenacao import quick_sort
                resultado, tempo = quick_sort(lista.copy(), tamanho, mostrar_passos)
                print('Resultado:', resultado, '\nTempo:', tempo)
            elif escolha == '6':
                from src.model.ordenacao import heap_sort
                resultado, tempo = heap_sort(lista.copy(), tamanho, mostrar_passos)
                print('Resultado:', resultado, '\nTempo:', tempo)
        elif opcao == '2':  # Busca
            escolha = menu_busca()
            if escolha is None or escolha == '0':
                continue
            tamanho = int(input('Tamanho da lista: '))

            print("Opções de ordenação:")
            print("1 - Ordenado Crescente")
            print("2 - Ordenado Decrescente")
            print("3 - Quase Ordenado")
            print("4 - Aleatório")

            ordenacao = input("Escolha uma opção (1-4): ").strip()
            if ordenacao == '1':
                ordenado = True
                crescente = True
                decrescente = False
                quase_ordenado = False
            elif ordenacao == '2':
                ordenado = True
                crescente = False
                decrescente = True
                quase_ordenado = False
            elif ordenacao == '3':
                ordenado = True
                crescente = False
                decrescente = False
                quase_ordenado = True
            elif ordenacao == '4':
                ordenado = False
                crescente = False
                decrescente = False
                quase_ordenado = False
            else:
                print("Opção inválida. Usando lista aleatória.")
                ordenado = False
                crescente = False
                decrescente = False
                quase_ordenado = False

            lista = gerar_lista(tamanho, ordenado=ordenado, crescente=crescente, decrescente=decrescente, quase_ordenado=quase_ordenado)
            print('Lista gerada:', lista)
            valor = int(input('Valor a buscar: '))
            if escolha == '1':
                from src.model.busca import busca_linear
                idx, comp = busca_linear(lista, valor)
                print(f'Índice: {idx}, Comparações: {comp}')
            elif escolha == '2':
                from src.model.busca import busca_binaria
                lista_ordenada = sorted(lista)
                print('Lista usada para busca binária (ordenada):', lista_ordenada)
                idx, comp = busca_binaria(lista_ordenada, valor)
                print(f'Índice: {idx}, Comparações: {comp}')

        elif opcao == '3':  # Otimização
            escolha = menu_otimizacao()
            if escolha is None or escolha == '0':
                continue
            if escolha == '1':
                from src.model.otimizacao import mochila_01
                n = int(input('Número de itens: '))
                pesos = [int(input(f'Peso do item {i+1}: ')) for i in range(n)]
                valores = [int(input(f'Valor do item {i+1}: ')) for i in range(n)]
                capacidade = int(input('Capacidade da mochila: '))
                valor_total, itens, _ = mochila_01(pesos, valores, capacidade)
                print(f'Valor total: {valor_total}, Itens selecionados: {itens}')
            elif escolha == '2':
                from src.model.otimizacao import mochila_fracionaria
                n = int(input('Número de itens: '))
                pesos = [float(input(f'Peso do item {i+1}: ')) for i in range(n)]
                valores = [float(input(f'Valor do item {i+1}: ')) for i in range(n)]
                capacidade = float(input('Capacidade da mochila: '))
                valor_total, itens = mochila_fracionaria(pesos, valores, capacidade)
                print(f'Valor total: {valor_total}, Itens (índice, quantidade): {itens}')
            elif escolha == '3':
                from src.model.otimizacao import corte_de_barras
                n = int(input('Número de tamanhos de corte possíveis: '))
                precos = [int(input(f'Preço para barra de tamanho {i+1}: ')) for i in range(n)]
                tamanho_barra = int(input('Tamanho da barra: '))
                t0 = time.perf_counter()
                valor, cortes = corte_de_barras(precos, tamanho_barra)
                t1 = time.perf_counter()
                print(f'Corte de Barras: Valor máximo={valor}, Cortes={cortes}, Tempo={t1 - t0:.6f}s')
            elif escolha == '4':
                from src.model.otimizacao import troco_minimo
                valor = int(input('Valor do troco: '))
                moedas = list(map(int, input('Moedas disponíveis (separadas por espaço): ').split()))
                qtd, combinacao = troco_minimo(valor, moedas)
                print(f'Mínimo de moedas: {qtd}, Combinação: {combinacao}')
                
        elif opcao == '4':  # Caixeiro Viajante
            escolha = menu_caixeiro()
            if escolha is None or escolha == '0':
                continue
            n = int(input('Número de cidades: '))
            cidades = []
            for i in range(n):
                x = float(input(f'Coordenada x da cidade {i}: '))
                y = float(input(f'Coordenada y da cidade {i}: '))
                cidades.append((x, y))
            if escolha == '1':
                from src.model.caixeiro import forca_bruta_tsp
                custo, rota = forca_bruta_tsp(cidades)
                print(f'Custo: {custo}, Rota: {rota}')
            elif escolha == '2':
                from src.model.caixeiro import nearest_neighbor
                rota, custo = nearest_neighbor(cidades)
                print(f'Custo: {custo}, Rota: {rota}')
            elif escolha == '3':
                from src.model.caixeiro import held_karp
                custo, rota = held_karp(cidades)
                print(f'Custo: {custo}, Rota: {rota}')
            elif escolha == '4':
                from src.model.caixeiro import two_opt
                rota, custo = two_opt(cidades)
                print(f'Custo: {custo}, Rota: {rota}')
        elif opcao == '5':  # Extras
            while True:
                escolha = menu_extras()
                if escolha is None or escolha == '0':
                    break
                if escolha == '1':
                    from src.model.extras import salvar_instancia
                    n = int(input('Número de cidades: '))
                    cidades = []
                    for i in range(n):
                        x = float(input(f'Coordenada x da cidade {i}: '))
                        y = float(input(f'Coordenada y da cidade {i}: '))
                        cidades.append((x, y))
                    nome = input('Nome do arquivo para salvar (ex: instancia.json): ').strip() or 'instancia.json'
                    salvar_instancia(cidades, nome)
                    print(f'Instância salva em {nome}')
                elif escolha == '2':
                    from src.model.extras import carregar_instancia
                    nome = input('Nome do arquivo para carregar (ex: instancia.json): ').strip() or 'instancia.json'
                    cidades = carregar_instancia(nome)
                    print('Instância carregada:', cidades)
                    
                    # Novo menu para escolher métodos do caixeiro
                    print('Escolha os métodos do Caixeiro Viajante para executar:')
                    print('1 - Força Bruta')
                    print('2 - Vizinho Mais Próximo')
                    print('3 - Held-Karp')
                    print('4 - Two-opt')
                    print('5 - Todos')
                    metodos = input('Digite os números dos métodos separados por vírgula (ex: 1,2,4 ou 5 para todos): ').strip()
                    if metodos == '5':
                        metodos = ['1', '2', '3', '4']
                    else:
                        metodos = [m.strip() for m in metodos.split(',')]
                    resultados = {}
                    tempos = {}
                    import time
                    for m in metodos:
                        if m == '1':
                            from src.model.caixeiro import forca_bruta_tsp
                            t0 = time.perf_counter()
                            custo, rota = forca_bruta_tsp(cidades)
                            t1 = time.perf_counter()
                            resultados['Força Bruta'] = custo
                            tempos['Força Bruta'] = t1 - t0
                            print(f'Força Bruta: custo={custo}, rota={rota}, tempo={t1-t0:.6f}s')
                        elif m == '2':
                            from src.model.caixeiro import nearest_neighbor
                            t0 = time.perf_counter()
                            rota, custo = nearest_neighbor(cidades)
                            t1 = time.perf_counter()
                            resultados['Vizinho Mais Próximo'] = custo
                            tempos['Vizinho Mais Próximo'] = t1 - t0
                            print(f'Vizinho Mais Próximo: custo={custo}, rota={rota}, tempo={t1-t0:.6f}s')
                        elif m == '3':
                            from src.model.caixeiro import held_karp
                            t0 = time.perf_counter()
                            custo, rota = held_karp(cidades)
                            t1 = time.perf_counter()
                            resultados['Held-Karp'] = custo
                            tempos['Held-Karp'] = t1 - t0
                            print(f'Held-Karp: custo={custo}, rota={rota}, tempo={t1-t0:.6f}s')
                        elif m == '4':
                            from src.model.caixeiro import two_opt
                            t0 = time.perf_counter()
                            rota, custo = two_opt(cidades)
                            t1 = time.perf_counter()
                            resultados['Two-opt'] = custo
                            tempos['Two-opt'] = t1 - t0
                            print(f'Two-opt: custo={custo}, rota={rota}, tempo={t1-t0:.6f}s')
                    # Menu para salvar tempos e plotar gráfico
                    print('\nDeseja salvar os tempos de execução em CSV? (s/n)')
                    if input().strip().lower() == 's':
                        import csv
                        nome_csv = input('Nome do arquivo CSV (ex: tempos.csv): ').strip() or 'tempos.csv'
                        with open(nome_csv, 'w', newline='') as f:
                            writer = csv.writer(f)
                            writer.writerow(['Método', 'Tempo (s)'])
                            for metodo, tempo in tempos.items():
                                writer.writerow([metodo, tempo])
                        print(f'Tempos salvos em {nome_csv}')
                    print('Deseja plotar o gráfico comparativo dos tempos? (s/n)')
                    if input().strip().lower() == 's':
                        import matplotlib.pyplot as plt
                        plt.bar(tempos.keys(), tempos.values())
                        plt.ylabel('Tempo (s)')
                        plt.title('Comparativo de Tempos dos Métodos TSP')
                        plt.show()
                elif escolha == '3':
                    from src.model.extras import exportar_resultado_csv
                    rota = input('Digite a rota (ex: 0,1,2,0): ').strip()
                    rota = [int(x) for x in rota.split(',')]
                    custo = float(input('Digite o custo total: '))
                    nome = input('Nome do arquivo CSV (ex: resultado.csv): ').strip() or 'resultado.csv'
                    exportar_resultado_csv(rota, custo, nome)
                    print(f'Resultado exportado para {nome}')
                elif escolha == '4':
                    from src.model.extras import plot_comparativo
                    print("Qual metodos você deseja comparar?")
                    print("1 - Operações de busca")
                    print("2 - Operações de ordenação")
                    print("3 - Operações de otimização")
                    print("4 - Caixeiro Viajante")
                    print("0 - Voltar")
                    escolha = input("Escolha uma opção: ").strip()

                    if escolha == '0':
                        continue
                    elif escolha == '1':
                        tempos = []

                        print("Digite o numero de elementos na lista:")
                        n = int(input().strip())
                        print("Digite o valor a ser buscado:")
                        valor = int(input().strip())
                        lista = gerar_lista(n, ordenado=True, crescente=True)
                        print("Lista gerada:", lista)

                        from src.model.busca import busca_linear, busca_binaria
                        import time

                        # Busca Linear
                        t0 = time.perf_counter()
                        idx_linear, comp_linear = busca_linear(lista, valor)
                        t1 = time.perf_counter()
                        tempos.append(('Busca Linear', t1 - t0))
                        print(f'Busca Linear: Índice={idx_linear}, Comparações={comp_linear}, Tempo={t1 - t0:.6f}s')
                        # Busca Binária
                        lista_ordenada = sorted(lista)
                        t0 = time.perf_counter()
                        idx_binaria, comp_binaria = busca_binaria(lista_ordenada, valor)
                        t1 = time.perf_counter()
                        tempos.append(('Busca Binária', t1 - t0))
                        print(f'Busca Binária: Índice={idx_binaria}, Comparações={comp_binaria}, Tempo={t1 - t0:.6f}s')
                        plot_comparativo(dict(tempos))
                    elif escolha == '2':
                        tempos = []

                        print("Digite o numero de elementos na lista:")
                        n = int(input().strip())
                        lista = gerar_lista(n, ordenado=True, crescente=True)
                        print("Lista gerada:", lista)

                        from src.model.ordenacao import bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort, heap_sort
                        import time

                        # Bubble Sort
                        t0 = time.perf_counter()
                        resultado_bubble, tempo_bubble = bubble_sort(lista.copy(), n, mostrar_passos=False)
                        t1 = time.perf_counter()
                        tempos.append(('Bubble Sort', t1 - t0))
                        print(f'Bubble Sort: Resultado={resultado_bubble}, Tempo={t1 - t0:.6f}s')

                        # Selection Sort
                        t0 = time.perf_counter()
                        resultado_selection, tempo_selection = selection_sort(lista.copy(), n, mostrar_passos=False)
                        t1 = time.perf_counter()
                        tempos.append(('Selection Sort', t1 - t0))
                        print(f'Selection Sort: Resultado={resultado_selection}, Tempo={t1 - t0:.6f}s')

                        # Insertion Sort
                        t0 = time.perf_counter()
                        resultado_insertion, tempo_insertion = insertion_sort(lista.copy(), n, mostrar_passos=False)
                        t1 = time.perf_counter()
                        tempos.append(('Insertion Sort', t1 - t0))
                        print(f'Insertion Sort: Resultado={resultado_insertion}, Tempo={t1 - t0:.6f}s')

                        # Merge Sort
                        t0 = time.perf_counter()
                        resultado_merge, tempo_merge = merge_sort(lista.copy(), n, mostrar_passos=False)
                        t1 = time.perf_counter()
                        tempos.append(('Merge Sort', t1 - t0))
                        print(f'Merge Sort: Resultado={resultado_merge}, Tempo={t1 - t0:.6f}s')

                        # Quick Sort
                        t0 = time.perf_counter()
                        resultado_quick, tempo_quick = quick_sort(lista.copy(), n, mostrar_passos=False)
                        t1 = time.perf_counter()
                        tempos.append(('Quick Sort', t1 - t0))
                        print(f'Quick Sort: Resultado={resultado_quick}, Tempo={t1 - t0:.6f}s')

                        # Heap Sort
                        t0 = time.perf_counter()
                        resultado_heap, tempo_heap = heap_sort(lista.copy(), n, mostrar_passos=False)
                        t1 = time.perf_counter()
                        tempos.append(('Heap Sort', t1 - t0))
                        print(f'Heap Sort: Resultado={resultado_heap}, Tempo={t1 - t0:.6f}s')
                        plot_comparativo(dict(tempos))
                    elif escolha == '3':
                        tempos = []

                        print("Digite o numero de itens:")
                        n = int(input().strip())
                        pesos = [int(input(f'Peso do item {i+1}: ')) for i in range(n)]
                        valores = [int(input(f'Valor do item {i+1}: ')) for i in range(n)]
                        capacidade = int(input('Capacidade da mochila: '))

                        from src.model.otimizacao import mochila_01, mochila_fracionaria, corte_de_barras, troco_minimo
                        import time

                        # Mochila 01
                        t0 = time.perf_counter()
                        valor_total_01, itens_01, _ = mochila_01(pesos, valores, capacidade)
                        t1 = time.perf_counter()
                        tempos.append(('Mochila 01', t1 - t0))
                        print(f'Mochila 01: Valor total={valor_total_01}, Itens={itens_01}, Tempo={t1 - t0:.6f}s')

                        # Mochila Fracionária
                        t0 = time.perf_counter()
                        valor_total_frac, itens_frac = mochila_fracionaria(pesos, valores, capacidade)
                        t1 = time.perf_counter()
                        tempos.append(('Mochila Fracionária', t1 - t0))
                        print(f'Mochila Fracionária: Valor total={valor_total_frac}, Itens={itens_frac}, Tempo={t1 - t0:.6f}s')

                        # Corte de Barras
                        precos = [int(input(f'Preço do tamanho {i+1}: ')) for i in range(n)]
                        tamanhos = [int(input(f'Tamanho {i+1}: ')) for i in range(n)]
                        tamanho_barra = int(input('Tamanho da barra: '))
                        t0 = time.perf_counter()
                        valor_corte, cortes_corte = corte_de_barras(precos, tamanhos, tamanho_barra)
                        t1 = time.perf_counter()
                        tempos.append(('Corte de Barras', t1 - t0))
                        print(f'Corte de Barras: Valor máximo={valor_corte}, Cortes={cortes_corte}, Tempo={t1 - t0:.6f}s')

                        # Troco Mínimo
                        valor_troco = int(input('Valor do troco: '))
                        moedas = list(map(int, input('Moedas disponíveis (separadas por espaço): ').split()))
                        t0 = time.perf_counter()
                        troco_minimo(valor_troco, moedas)
                        t1 = time.perf_counter()
                        tempos.append(('Troco Mínimo', t1 - t0))
                        print(f'Troco Mínimo: Tempo={t1 - t0:.6f}s')
                        plot_comparativo(dict(tempos))  
                    elif escolha == '4':
                        tempos = []

                        print("Digite o numero de cidades:")
                        n = int(input().strip())
                        cidades = []
                        for i in range(n):
                            x = float(input(f'Coordenada x da cidade {i}: '))
                            y = float(input(f'Coordenada y da cidade {i}: '))
                            cidades.append((x, y))

                        from src.model.caixeiro import forca_bruta_tsp, nearest_neighbor, held_karp, two_opt
                        import time

                        # Força Bruta
                        t0 = time.perf_counter()
                        custo_fb, rota_fb = forca_bruta_tsp(cidades)
                        t1 = time.perf_counter()
                        tempos.append(('Força Bruta', t1 - t0))
                        print(f'Força Bruta: Custo={custo_fb}, Rota={rota_fb}, Tempo={t1 - t0:.6f}s')

                        # Vizinho Mais Próximo
                        t0 = time.perf_counter()
                        rota_nn, custo_nn = nearest_neighbor(cidades)
                        t1 = time.perf_counter()
                        tempos.append(('Vizinho Mais Próximo', t1 - t0))
                        print(f'Vizinho Mais Próximo: Custo={custo_nn}, Rota={rota_nn}, Tempo={t1 - t0:.6f}s')

                        # Held-Karp
                        t0 = time.perf_counter()
                        custo_hk, rota_hk = held_karp(cidades)
                        t1 = time.perf_counter()
                        tempos.append(('Held-Karp', t1 - t0))
                        print(f'Held-Karp: Custo={custo_hk}, Rota={rota_hk}, Tempo={t1 - t0:.6f}s')

                        # Two-opt
                        t0 = time.perf_counter()
                        rota_to, custo_to = two_opt(cidades)
                        t1 = time.perf_counter()
                        tempos.append(('Two-opt', t1 - t0))
                        print(f'Two-opt: Custo={custo_to}, Rota={rota_to}, Tempo={t1 - t0:.6f}s')
                        
                        plot_comparativo(dict(tempos))

                    else:
                        print("Opção inválida. Tente novamente.")
                        continue
                else:
                    print("Opcao invalida. Tente novamente.")
                    continue

if __name__ == '__main__':
    main()








