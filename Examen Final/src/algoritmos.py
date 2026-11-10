def ordenamiento_burbuja(lista_original):
    """
    Ordena una copia de la lista usando Bubble Sort.
    Retorna: (lista_ordenada, total_iteraciones)
    """
    arr = lista_original.copy()
    n = len(arr)
    iteraciones = 0
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            iteraciones += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr, iteraciones

def ordenamiento_seleccion(lista_original):
    """
    Ordena una copia de la lista usando Selection Sort.
    Retorna: (lista_ordenada, total_iteraciones)
    """
    arr = lista_original.copy()
    n = len(arr)
    iteraciones = 0
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            iteraciones += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr, iteraciones