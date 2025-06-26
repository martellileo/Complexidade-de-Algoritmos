
import networkx as nx
import matplotlib.pyplot as plt
import itertools
import time

# Grafos extraídos do PDF
grafo_1 = {
    'A': {'B', 'D'},
    'B': {'A', 'C'},
    'C': {'B', 'D'},
    'D': {'C', 'A'}
}

grafo_2 = {
    'A': {'B'},
    'B': {'A', 'C'},
    'C': {'B', 'D'},
    'D': {'C'}
}

grafo_3 = {
    'A': {'B', 'C'},
    'B': {'A', 'C'},
    'C': {'A', 'B', 'D'},
    'D': {'C', 'E'},
    'E': {'D'}
}

grafo_4 = {
    'A': {'B', 'E'},
    'B': {'A', 'C'},
    'C': {'B', 'D'},
    'D': {'C', 'E'},
    'E': {'D', 'A'}
}

grafo_5 = {
    'A': {'B', 'C', 'D', 'E'},
    'B': {'A'},
    'C': {'A'},
    'D': {'A'},
    'E': {'A'}
}

grafo_6 = {
    'A': {'B', 'F'},
    'B': {'A', 'C'},
    'C': {'B', 'D'},
    'D': {'C', 'E'},
    'E': {'D', 'F'},
    'F': {'E', 'A'}
}

grafo_7 = {
    'A': {'B'},
    'B': {'A', 'C'},
    'C': {'B', 'E'},
    'D': {'E'},
    'E': {'C', 'D'}
}

grafo_8 = {
    'A': {'B', 'C', 'D'},
    'B': {'A', 'C'},
    'C': {'A', 'B', 'D'},
    'D': {'A', 'C'}
}

grafo_9 = {
    'A': {'B', 'C'},
    'B': {'A', 'C'},
    'C': {'A', 'B', 'D'},
    'D': {'C', 'E'},
    'E': {'D'}
}

grafo_10 = {
    'A': {'B', 'F'},
    'B': {'A', 'C', 'E'},
    'C': {'B', 'D', 'F'},
    'D': {'C', 'E'},
    'E': {'B', 'D', 'F'},
    'F': {'A', 'C', 'E'}
}

# Dicionário de todos os grafos para exportação
grafos = {
    "Grafo_1": grafo_1,
    "Grafo_2": grafo_2,
    "Grafo_3": grafo_3,
    "Grafo_4": grafo_4,
    "Grafo_5": grafo_5,
    "Grafo_6": grafo_6,
    "Grafo_7": grafo_7,
    "Grafo_8": grafo_8,
    "Grafo_9": grafo_9,
    "Grafo_10": grafo_10
}

# Função para exportar grafos para PNG

import itertools

def verificar_hamiltoniano(G):
    # Verifica se o grafo é hamiltoniano
    nodes = list(G.nodes)
    for ciclo in itertools.permutations(nodes):
        # Verifica se o ciclo forma um caminho válido e retorna ao nó inicial
        if all(G.has_edge(ciclo[i], ciclo[i + 1]) for i in range(len(ciclo) - 1)) and G.has_edge(ciclo[-1], ciclo[0]):
            return True
    return False

def exportar_grafos_para_png():
    for nome, grafo in grafos.items():
        G = nx.Graph()
        for node in grafo:
            for neighbor in grafo[node]:
                G.add_edge(node, neighbor)

        pos = nx.spring_layout(G, seed=42)
        plt.figure(figsize=(5, 5))

        # Desenhar o grafo com os nós mostrando as letras
        nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=700, font_size=10)

        # Adicionar as distâncias como legendas
        edge_labels = {(u, v): f"{nx.shortest_path_length(G, u, v)}" for u, v in G.edges()}
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

        # Verificar se o grafo é hamiltoniano
        hamiltoniano = verificar_hamiltoniano(G)
        texto = "Hamiltoniano" if hamiltoniano else "Não Hamiltoniano"

        # Adicionar texto no canto superior esquerdo
        plt.text(0.01, 0.95, texto, color='red', fontsize=12, transform=plt.gcf().transFigure)

        plt.title(nome)
        plt.savefig(f"{nome}.png")
        plt.close()
    print("Grafos exportados como PNG na pasta do projeto.")

# Python
def calcular_e_mostrar_grafo(numero_grafo):
    nome_grafo = f"Grafo_{numero_grafo}"
    if nome_grafo in grafos:
        grafo = grafos[nome_grafo]
        G = nx.Graph()
        for node in grafo:
            for neighbor in grafo[node]:
                G.add_edge(node, neighbor)

        pos = nx.spring_layout(G, seed=42)
        plt.figure(figsize=(5, 5))

        # Desenhar o grafo com os nós mostrando as letras
        nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=700, font_size=10)

        # Adicionar as distâncias como legendas
        edge_labels = {(u, v): f"{nx.shortest_path_length(G, u, v)}" for u, v in G.edges()}
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

        # Verificar se o grafo é hamiltoniano
        hamiltoniano = verificar_hamiltoniano(G)
        texto = "Hamiltoniano" if hamiltoniano else "Não Hamiltoniano"

        # Adicionar texto no canto superior esquerdo
        plt.text(0.01, 0.95, texto, color='red', fontsize=12, transform=plt.gcf().transFigure)

        plt.title(nome_grafo)
        plt.show()
    else:
        print("Número de grafo inválido. Tente novamente.")

# Menu atualizado
while True:
    print("\nMenu:")
    print("0 - Sair")
    print("1 - Calcular e mostrar grafo")
    print("2 - Exportar grafos para PNG")

    option = input("Escolha uma opção: ")

    if option == '0':
        print("Saindo...")
        break
    elif option == '1':
        numero_grafo = input("Digite o número do grafo (1 a 10): ")
        if numero_grafo.isdigit() and 1 <= int(numero_grafo) <= 10:
            calcular_e_mostrar_grafo(numero_grafo)
        else:
            print("Número inválido. Tente novamente.")
    elif option == '2':
        exportar_grafos_para_png()
    else:
        print("Opção inválida. Tente novamente.")