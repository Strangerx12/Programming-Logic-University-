from src.generador import generar_lista
from src.comparador import mostrar_detalles_algoritmo, comparar_ambos
from src.complejidad import mostrar_tabla_complejidad, obtener_complejidad

def sub_menu_algoritmo(nombre_algoritmo, lista_desordenada):
    """Submenú dinámico para el algoritmo seleccionado."""
    while True:
        print(f"\n--- SUBMENÚ: {nombre_algoritmo.upper()} ---")
        print("1. Ver lista desordenada actual")
        print("2. Ejecutar ordenamiento (Ver lista ordenada e iteraciones)")
        print("3. Ver complejidad teórica y estabilidad del algoritmo")
        print("4. Volver al menú principal")
        
        opc = input("Seleccione una opción (1-4): ").strip()
        
        if opc == "1":
            print(f"\n📌 Lista desordenada actual: {lista_desordenada}")
        elif opc == "2":
            mostrar_detalles_algoritmo(nombre_algoritmo, lista_desordenada)
        elif opc == "3":
            obtener_complejidad(nombre_algoritmo)
        elif opc == "4":
            break
        else:
            print("\n[!] Opción no válida.")

def main():
    lista_desordenada = generar_lista(10)
    
    while True:
        print("\n==========================================")
        print("    MENÚ PRINCIPAL - ORDENAMIENTO        ")
        print("==========================================")
        print(f"Lista desordenada actual (10 elementos): {lista_desordenada}")
        print("------------------------------------------")
        print("1. Seleccionar algoritmo: Ordenamiento por Burbuja")
        print("2. Seleccionar algoritmo: Ordenamiento por Selección")
        print("3. Comparar iteraciones de ambos algoritmos")
        print("4. Ver tabla completa de complejidades teóricas")
        print("5. Generar nueva lista desordenada")
        print("6. Salir")
        print("------------------------------------------")
        
        opcion = input("Elija una opción (1-6): ").strip()
        
        if opcion == "1":
            sub_menu_algoritmo("Burbuja", lista_desordenada)
        elif opcion == "2":
            sub_menu_algoritmo("Selección", lista_desordenada)
        elif opcion == "3":
            comparar_ambos(lista_desordenada)
        elif opcion == "4":
            mostrar_tabla_complejidad()
        elif opcion == "5":
            lista_desordenada = generar_lista(10)
            print(f"\n[✓] Nueva lista desordenada generada: {lista_desordenada}")
        elif opcion == "6":
            print("\n¡Programa finalizado!")
            break
        else:
            print("\n[!] Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()