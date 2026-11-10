import random

def generar_lista(tamano=10, limite_inferior=1, limite_superior=100):
    """Genera una lista desordenada de enteros aleatorios."""
    return [random.randint(limite_inferior, limite_superior) for _ in range(tamano)]