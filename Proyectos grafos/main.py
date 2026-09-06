import csv
import networkx as nx
import matplotlib.pyplot as plt
from src.validaciones import verificar_camino_euler, verificar_camino_hamilton
import os

def exportar_matriz_csv(grafo):
    dir_actual = os.path.dirname(os.path.abspath(__file__))
    ruta_db = os.path.join(dir_actual, 'db')
    os.makedirs(ruta_db, exist_ok=True)
    
    ruta_archivo = os.path.join(ruta_db, 'matriz.csv')
    nodos = sorted(list(grafo.nodes()))
    
    with open(ruta_archivo, mode='w', newline='', encoding='utf-8') as archivo:
        escritor = csv.writer(archivo)
        for u in nodos:
            fila = [1 if grafo.has_edge(u, v) else 0 for v in nodos]
            escritor.writerow(fila)
            
    print(f"[+] Archivo guardado con éxito en: {ruta_archivo}")

def main():
    print("--- ANÁLISIS DE REDES: CLUB DE KARATE DE ZACHARY ---")
    
    G = nx.karate_club_graph()
    exportar_matriz_csv(G)
    
    # Validar Euler
    tiene_euler, impares = verificar_camino_euler(G)
    print(f"Camino Euleriano: {'SÍ' if tiene_euler else 'NO'} (Nodos impares: {impares})")
    
    # Validar Hamilton (Reactivo y funcionando)
    print("Calculando camino Hamiltoniano (procesando árbol de decisiones...)")
    tiene_hamilton = verificar_camino_hamilton(G)
    print(f"Camino Hamiltoniano: {'SÍ' if tiene_hamilton else 'NO'}")
    
    # Generar Gráfico
    plt.figure(figsize=(9, 6))
    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_color='#ff7f0e', edge_color='#1f77b4', font_weight='bold')
    plt.show()

if __name__ == "__main__":
    main()