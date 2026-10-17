import pygame

# Constantes de configuración
WIDTH, HEIGHT = 800, 600
FPS = 60

# Paleta de colores
WHITE = (255, 255, 255)
BLACK = (20, 20, 20)
BLUE = (65, 105, 225)
GREEN = (46, 204, 113)
RED = (231, 76, 60)

def init_window():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Animación Merge Sort")
    clock = pygame.time.Clock()
    return screen, clock

def draw_array(screen, arr, color_positions={}, default_color=BLUE):
    screen.fill(BLACK)
    if not arr: return
    
    bar_width = WIDTH / len(arr)
    max_val = max(arr)
    
    for i, val in enumerate(arr):
        height = (val / max_val) * (HEIGHT - 50) 
        x = i * bar_width
        y = HEIGHT - height
        
        color = color_positions.get(i, default_color)
        pygame.draw.rect(screen, color, (x, y, bar_width - 1, height))
    
    pygame.display.flip()
    
def init_window():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Animación Merge Sort")
    clock = pygame.time.Clock()
    return screen, clock  # <- ESTA ES LA LÍNEA QUE FALTA