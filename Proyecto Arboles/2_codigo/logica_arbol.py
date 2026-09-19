class NodoArbol:
    """Representa un nodo dentro de la estructura jerárquica del árbol"""
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)


class ArbolDecision:
    """Clase principal para gestionar el árbol de decisiones"""
    def __init__(self):
        self.nodos = {}

    def obtener_o_crear_nodo(self, valor):
        if valor not in self.nodos:
            self.nodos[valor] = NodoArbol(valor)
        return self.nodos[valor]

    def agregar_relacion(self, padre, hijo):
        nodo_padre = self.obtener_o_crear_nodo(padre.strip())
        nodo_hijo = self.obtener_o_crear_nodo(hijo.strip())
        nodo_padre.agregar_hijo(nodo_hijo)