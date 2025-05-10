import pygame
import math

def ejecutar_juego(boat_color):
    pygame.init()
    WIDTH, HEIGHT = 800, 600
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Juego de Regata")
    clock = pygame.time.Clock()

    WHITE = (255, 255, 255)
    BLUE = (100, 149, 237)

    boat_pos = [WIDTH // 2, HEIGHT // 2]
    boat_angle = 0  # grados
    wind_angle = 45
    wind_strength = 1.5

    def move_boat(pos, angle):
        rad = math.radians(angle)
        dx = math.cos(rad)
        dy = math.sin(rad)
        angle_diff = abs((angle - wind_angle + 360) % 360)
        effectiveness = max(0.2, math.cos(math.radians(angle_diff)))  # 0.2 a 1
        pos[0] += dx * wind_strength * effectiveness * 10
        pos[1] += dy * wind_strength * effectiveness * 10
        return pos

    def draw_boat(pos, angle):
        rad = math.radians(angle)
        size = 20
        tip = (pos[0] + math.cos(rad) * size, pos[1] + math.sin(rad) * size)
        left = (pos[0] + math.cos(rad + 2.5) * size, pos[1] + math.sin(rad + 2.5) * size)
        right = (pos[0] + math.cos(rad - 2.5) * size, pos[1] + math.sin(rad - 2.5) * size)
        pygame.draw.polygon(win, boat_color, [tip, left, right])

    def draw_wind_arrow():
        wx = math.cos(math.radians(wind_angle)) * 50
        wy = math.sin(math.radians(wind_angle)) * 50
        pygame.draw.line(win, WHITE, (50, 50), (50 + wx, 50 + wy), 3)

    running = True
    while running:
        win.fill(BLUE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            boat_angle = (boat_angle - 5) % 360
            pygame.time.wait(200)
        if keys[pygame.K_RIGHT]:
            boat_angle = (boat_angle + 5) % 360
            pygame.time.wait(200)
        if keys[pygame.K_SPACE]:
            boat_pos = move_boat(boat_pos, boat_angle)
            pygame.time.wait(200)

        draw_boat(boat_pos, boat_angle)
        draw_wind_arrow()

        pygame.display.update()
        clock.tick(30)

    pygame.quit()
