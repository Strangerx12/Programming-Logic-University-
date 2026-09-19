import sys
import os
import csv
import networkx as nx
import matplotlib.pyplot as plt

# Vinculamos la carpeta de código correctamente
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../2_codigo')))
from logica_arbol import ArbolDecision

def ejecutar_sistema_arbol():
    mi_arbol = ArbolDecision()
    
    # Ruta absoluta al archivo CSV en la base de datos
    ruta_archivo = os.path.abspath(os.path.join(os.path.dirname(__file__), '../1_base_de_datos/reglas_arbol.csv'))
    
    print(f"📂 Leyendo base de datos CSV desde: {ruta_archivo}\n")
    
    try:
        with open(ruta_archivo, mode='r', encoding='utf-8') as archivo_csv:
            lector = csv.DictReader(archivo_csv) # Lee el archivo usando los encabezados (padre, hijo)
            for fila in lector:
                padre = fila['padre']
                hijo = fila['hijo']
                mi_arbol.agregar_relacion(padre, hijo)
    except FileNotFoundError:
        print("❌ Error: No se encontró el archivo CSV de base de datos.")
        return

    # Generar Gráfico Visual del Árbol con NetworkX y Matplotlib
    print("🎨 Generando gráfico visual del Árbol de Decisión...")
    
    G = nx.DiGraph()  # Grafo dirigido para respetar la jerarquía del árbol
    for padre_str, nodo_obj in mi_arbol.nodos.items():
        for hijo_obj in nodo_obj.hijos:
            G.add_edge(padre_str, hijo_obj.valor)

    plt.figure(figsize=(12, 7))
    
    # Posicionamiento de nodos
    pos = nx.spring_layout(G, seed=42)

    # Dibujar componentes explícitamente
    nx.draw_networkx_nodes(G, pos, node_size=3500, node_color='#bde0fe', node_shape='o')
    nx.draw_networkx_edges(G, pos, width=2, edge_color='#6c757d', arrows=True, arrowsize=20)
    nx.draw_networkx_labels(G, pos, font_size=8, font_weight='bold')
    
    plt.title("Árbol de Decisión (Base de datos CSV) - Fraudes Bancarios", fontsize=13, fontweight='bold')
    plt.axis('off')
    
    print("✅ ¡Gráfico generado con éxito! Se abrirá la ventana emergente.")
    plt.show()

if __name__ == "__main__":
    ejecutar_sistema_arbol()