# EXTRAS
import json
import matplotlib.pyplot as plt
import csv


def salvar_instancia(cidades, nome="instancia.json"):
    with open(nome, "w") as f:
        json.dump(cidades, f)

def carregar_instancia(nome="instancia.json"):
    with open(nome, "r") as f:
        return json.load(f)

def exportar_resultado_csv(rota: list[int], custo: float, nome="resultado.csv"):
    with open(nome, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Cidade"])
        for c in rota:
            writer.writerow([c])
        writer.writerow([])
        writer.writerow(["Custo total", custo])

def plot_comparativo(resultados: dict):
    nomes = list(resultados.keys())
    custos = [resultados[n] for n in nomes]

    plt.bar(nomes, custos)
    plt.ylabel("Custo Total")
    plt.title("Comparação de métodos TSP")
    plt.show()
