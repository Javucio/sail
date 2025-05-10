import pygame
from juego import ejecutar_juego

pygame.init()
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sail")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

WHITE = (255, 255, 255)
BLUE = (100, 149, 237)
BOAT_COLORS = [(200, 50, 50), (50, 200, 50), (50, 100, 200)]  # rojo, verde, azul

def draw_menu(selected_color_index):
    win.fill(BLUE)
    title = font.render("Elige el tipo de barco", True, WHITE)
    win.blit(title, (WIDTH//2 - title.get_width()//2, 150))

    # Dibujar un triángulo representando el barco
    center = [WIDTH // 2, HEIGHT // 2]
    size = 20
    color = BOAT_COLORS[selected_color_index]
    pygame.draw.polygon(win, color, [
        (center[0], center[1] - size),
        (center[0] - size, center[1] + size),
        (center[0] + size, center[1] + size)
    ])

    instr = font.render("Flechas izquierda o derecha para seleccionar | ENTER para empezar", True, WHITE)
    win.blit(instr, (WIDTH//2 - instr.get_width()//2, 400))
    pygame.display.update()

def menu():
    selected_index = 0
    running = True

    while running:
        draw_menu(selected_index)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                return

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    selected_index = (selected_index - 1) % len(BOAT_COLORS)
                elif event.key == pygame.K_RIGHT:
                    selected_index = (selected_index + 1) % len(BOAT_COLORS)
                elif event.key == pygame.K_RETURN:
                    color_elegido = BOAT_COLORS[selected_index]
                    ejecutar_juego(color_elegido)
                    running = False

menu()
