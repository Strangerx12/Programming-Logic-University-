def verificar_camino_euler(grafo):
    impares = 0
    for nodo, grado in grafo.degree():
        if grado % 2 != 0:
            impares += 1
            
    if impares == 0 or impares == 2:
        return True, impares
    return False, impares

def verificar_camino_hamilton(grafo):
    nodos = list(grafo.nodes())
    total_nodos = len(nodos)
    
    def backtrack(nodo_actual, visitados, camino):
        if len(camino) == total_nodos:
            return True
            
        for vecino in grafo.neighbors(nodo_actual):
            if vecino not in visitados:
                visitados.add(vecino)
                camino.append(vecino)
                
                if backtrack(vecino, visitados, camino):
                    return True
                    
                visitados.remove(vecino)
                camino.pop()
        return False

    for nodo_inicial in nodos:
        if backtrack(nodo_inicial, {nodo_inicial}, [nodo_inicial]):
            return True
            
    return False