COMPLEJIDADES = {
    "Burbuja": {
        "Mejor": "O(n)",
        "Promedio": "O(n²)",
        "Peor": "O(n²)",
        "Memoria extra": "O(1)",
        "Estable": "Sí"
    },
    "Selección": {
        "Mejor": "O(n²)",
        "Promedio": "O(n²)",
        "Peor": "O(n²)",
        "Memoria extra": "O(1)",
        "Estable": "No"
    }
}

def mostrar_tabla_complejidad():
    """Muestra la tabla comparativa de complejidad teórica."""
    print("\n" + "=" * 65)
    print("      COMPLEJIDAD ALGORÍTMICA Y PROPIEDADES (TEÓRICO)")
    print("=" * 65)
    print(f"{'Algoritmo':<12} | {'Mejor':<8} | {'Promedio':<8} | {'Peor':<8} | {'Memoria':<8} | {'Estable':<6}")
    print("-" * 65)
    for alg, datos in COMPLEJIDADES.items():
        print(f"{alg:<12} | {datos['Mejor']:<8} | {datos['Promedio']:<8} | {datos['Peor']:<8} | {datos['Memoria extra']:<8} | {datos['Estable']:<6}")
    print("=" * 65)
    print("💡 Nota: Un algoritmo 'Estable' conserva el orden relativo de elementos iguales.")

def obtener_complejidad(nombre_algoritmo):
    """Muestra la complejidad específica del algoritmo seleccionado."""
    datos = COMPLEJIDADES.get(nombre_algoritmo)
    if datos:
        print(f"\n--- Complejidad Teórica: {nombre_algoritmo} ---")
        print(f"• Mejor caso     : {datos['Mejor']}")
        print(f"• Caso promedio  : {datos['Promedio']}")
        print(f"• Peor caso      : {datos['Peor']}")
        print(f"• Memoria extra  : {datos['Memoria extra']}")
        print(f"• Estable        : {datos['Estable']}")