import pygame
import random
import sys
from visualizer import init_window, draw_array, HEIGHT, GREEN
from merge_sort import merge_sort_visual

def main():
    screen, clock = init_window()
    n = 100
    arr = [random.randint(20, HEIGHT) for _ in range(n)]
    
    running = True
    sorting = False
    generator = None
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not sorting:
                    sorting = True
                    generator = merge_sort_visual(arr, 0, len(arr) - 1)
                if event.key == pygame.K_r and not sorting:
                    arr = [random.randint(20, HEIGHT) for _ in range(n)]
        
        if sorting and generator:
            try:
                # Obtiene el arreglo actualizado y el diccionario de colores
                current_arr, color_dict = next(generator)
                draw_array(screen, current_arr, color_dict)
                clock.tick(60) # Controla la velocidad aquí
            except StopIteration:
                sorting = False
                draw_array(screen, arr, {i: GREEN for i in range(len(arr))})
        elif not sorting:
            draw_array(screen, arr)
            
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()