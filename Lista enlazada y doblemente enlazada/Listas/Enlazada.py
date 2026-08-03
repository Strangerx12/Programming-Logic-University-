# Definición del Nodo (cada eslabón de la cadena)
class Nodo: # Nodo contiene un dato y un apuntador al siguiente nodo
    def __init__(self, dato):
        self.dato = dato      # self permite que el objeto se refiera a cada mismo 
        self.siguiente = None # El apuntador al siguiente nodo (inicialmente vacío)

# Definición de la Lista Enlazada
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None    # El inicio de la lista (primer nodo)

    def agregar_al_inicio(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("None")

# --- Ejecución ---
mi_lista = ListaEnlazada()
mi_lista.agregar_al_inicio("Comprar pan")
mi_lista.agregar_al_inicio("Estudiar Python")
mi_lista.agregar_al_inicio("Pagar facturas")

print("Lista Enlazada de Tareas:")
mi_lista.mostrar()