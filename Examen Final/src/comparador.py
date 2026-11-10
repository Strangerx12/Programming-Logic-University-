from src.algoritmos import ordenamiento_burbuja, ordenamiento_seleccion
from src.complejidad import COMPLEJIDADES

def mostrar_detalles_algoritmo(nombre_algoritmo, lista_desordenada):
    """
    Despliega la lista desordenada, la ordenada, iteraciones reales y datos de la tabla.
    """
    if nombre_algoritmo == "Burbuja":
        ordenada, iteraciones = ordenamiento_burbuja(lista_desordenada)
    else:
        ordenada, iteraciones = ordenamiento_seleccion(lista_desordenada)

    info_teorica = COMPLEJIDADES[nombre_algoritmo]

    print("\n" + "=" * 55)
    print(f"       DETALLES DEL ALGORITMO: {nombre_algoritmo.upper()}")
    print("=" * 55)
    print(f"📌 Lista Desordenada : {lista_desordenada}")
    print(f"✅ Lista Ordenada    : {ordenada}")
    print(f"📊 Iteraciones usaras: {iteraciones}")
    print("-" * 55)
    print("  Datos teóricos del algoritmo:")
    print(f"   • Mejor caso: {info_teorica['Mejor']} | Promedio: {info_teorica['Promedio']} | Peor: {info_teorica['Peor']}")
    print(f"   • Memoria extra: {info_teorica['Memoria extra']} | Estable: {info_teorica['Estable']}")
    print("=" * 55)

def comparar_ambos(lista_desordenada):
    """
    Compara las iteraciones de ambos algoritmos y las contrasta con la tabla de complejidad.
    """
    ord_burbuja, iter_burbuja = ordenamiento_burbuja(lista_desordenada)
    ord_seleccion, iter_seleccion = ordenamiento_seleccion(lista_desordenada)

    print("\n" + "=" * 60)
    print("         COMPARACIÓN DE ITERACIONES Y COMPLEXIDAD")
    print("=" * 60)
    print(f"📌 Lista Desordenada : {lista_desordenada}\n")
    print(f"• Burbuja (Bubble Sort)    : {iter_burbuja} iteraciones | Mejor: O(n), Peor: O(n²)")
    print(f"• Selección (Selection Sort) : {iter_seleccion} iteraciones | Mejor: O(n²), Peor: O(n²)")
    print("-" * 60)

    if iter_burbuja < iter_seleccion:
        print(f"🏆 Burbuja fue más eficiente por {iter_seleccion - iter_burbuja} iteración(es) menos.")
    elif iter_seleccion < iter_burbuja:
        print(f"🏆 Selección fue más eficiente por {iter_burbuja - iter_seleccion} iteración(es) menos.")
    else:
        print(f"🤝 Ambos algoritmos usaron el mismo número de iteraciones ({iter_burbuja}).")
    print("=" * 60)