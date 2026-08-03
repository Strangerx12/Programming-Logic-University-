# Definición del Nodo Doble
class NodoDoble:
    def __init__(self, cancion):
        self.cancion = cancion  # Dato: nombre de la canción
        self.siguiente = None   # Puntero al nodo siguiente
        self.anterior = None    # Puntero al nodo anterior

# Definición de la Lista Doblemente Enlazada
class Playlist:
    def __init__(self): # init es una funcion de arranque automatico 
        self.cabeza = None

    def insertar_al_final(self, cancion):
        nuevo_nodo = NodoDoble(cancion)
        
        # Caso 1: Si la lista está vacía, el nuevo nodo es la cabeza
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return

        # Caso 2: Si hay elementos, recorremos hasta llegar al último
        actual = self.cabeza
        while actual.siguiente is not None:
            actual = actual.siguiente

        # Conectamos el último nodo con el nuevo nodo
        actual.siguiente = nuevo_nodo
        nuevo_nodo.anterior = actual  # Enlace hacia atrás clave de la lista doble

    def mostrar_adelante(self):
        actual = self.cabeza
        while actual:
            print(actual.cancion, end=" <-> ")
            actual = actual.siguiente
        print("None")

# --- Ejecución ---
mi_playlist = Playlist()
mi_playlist.insertar_al_final("Song A")
mi_playlist.insertar_al_final("Song B")
mi_playlist.insertar_al_final("Song C") # Inserción de un nuevo elemento

print("Playlist doblemente enlazada:")
mi_playlist.mostrar_adelante()