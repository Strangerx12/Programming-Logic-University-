def merge_sort_visual(arr, l, r):
    if l < r:
        m = l + (r - l) // 2
        yield from merge_sort_visual(arr, l, m)
        yield from merge_sort_visual(arr, m + 1, r)
        yield from merge(arr, l, m, r)

def merge(arr, l, m, r):
    left = arr[l:m + 1]
    right = arr[m + 1:r + 1]
    i = j = 0
    k = l
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        
        # Enviar estado actual: k (verde), comparaciones (rojo)
        yield arr, {k: (46, 204, 113), l+i: (231, 76, 60), m+1+j: (231, 76, 60)}
        k += 1
        
    while i < len(left):
        arr[k] = left[i]
        yield arr, {k: (46, 204, 113)}
        i += 1
        k += 1
        
    while j < len(right):
        arr[k] = right[j]
        yield arr, {k: (46, 204, 113)}
        j += 1
        k += 1