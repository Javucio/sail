import pygame
import math
import random

def ejecutar_juego(boat_color):
    pygame.init()
    WIDTH, HEIGHT = 800, 600
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sailmaniac")
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

        # Calcular la diferencia angular entre el barco y el viento
        angle_diff = abs((angle - wind_angle + 360) % 360)

        # Ajustar la lógica de efectividad según la dirección del viento
        if 150 <= angle_diff <= 210:  # Directamente contra el viento (viento de proa)
            effectiveness = 0.0  # Sin movimiento
        elif angle_diff < 30 or angle_diff > 330:  # Viento de popa (viento detrás del barco)
            effectiveness = 1.0  # Máxima efectividad
        elif 30 <= angle_diff <= 60 or 300 <= angle_diff <= 330:  # Ceñida (ángulos cercanos al viento de proa)
            effectiveness = 0.5  # Efectividad reducida
        else:
            # Efectividad basada en el coseno para otros ángulos
            effectiveness = max(0.2, math.cos(math.radians(angle_diff)))

        # Calcular el nuevo movimiento del barco
        new_x = pos[0] + dx * wind_strength * effectiveness * 10
        new_y = pos[1] + dy * wind_strength * effectiveness * 10

        # Limitar la posición del barco dentro de los límites de la pantalla
        pos[0] = max(0, min(WIDTH, new_x))
        pos[1] = max(0, min(HEIGHT, new_y))
        return pos
    
    def draw_ceñida_indicator(angle_diff):
        font_path = "assets/fonts/PressStart2P.ttf"  # Ruta a la fuente retro
        font = pygame.font.Font(font_path, 24)
        if 30 <= angle_diff <= 45:
            text = font.render("Ceñida activa", True, WHITE)
            win.blit(text, (10, HEIGHT - 80))

    def draw_boat(pos, angle):
        rad = math.radians(angle)
        size = 20
        tip = (pos[0] + math.cos(rad) * size, pos[1] + math.sin(rad) * size)
        left = (pos[0] + math.cos(rad + 2.5) * size, pos[1] + math.sin(rad + 2.5) * size)
        right = (pos[0] + math.cos(rad - 2.5) * size, pos[1] + math.sin(rad - 2.5) * size)
        pygame.draw.polygon(win, boat_color, [tip, left, right])

    def draw_wind_arrow():
        arrow_length = 50 + wind_strength * 10  # Tamaño proporcional a la fuerza del viento
        wx = math.cos(math.radians(wind_angle)) * arrow_length
        wy = math.sin(math.radians(wind_angle)) * arrow_length

        # Dibujar la línea principal de la flecha
        pygame.draw.line(win, WHITE, (50, 50), (50 + wx, 50 + wy), 3)

        # Dibujar las puntas de la flecha
        arrow_head_size = 10
        angle_offset = math.radians(20)  # Ángulo de las puntas de la flecha
        left_x = wx - math.cos(math.radians(wind_angle) - angle_offset) * arrow_head_size
        left_y = wy - math.sin(math.radians(wind_angle) - angle_offset) * arrow_head_size
        right_x = wx - math.cos(math.radians(wind_angle) + angle_offset) * arrow_head_size
        right_y = wy - math.sin(math.radians(wind_angle) + angle_offset) * arrow_head_size

        pygame.draw.line(win, WHITE, (50 + wx, 50 + wy), (50 + left_x, 50 + left_y), 3)
        pygame.draw.line(win, WHITE, (50 + wx, 50 + wy), (50 + right_x, 50 + right_y), 3)
        
        # Determinar la dirección del viento
        directions = [
            ((0 + 45) % 360, "Tramontana"), ((45 + 45) % 360, "Gregal"), ((90 + 45) % 360, "Levante"), ((135 + 45) % 360, "Siroco"),
            ((180 + 45) % 360, "Ostro"), ((225 + 45) % 360, "Lebeche"), ((270 + 45) % 360, "Poniente"), ((315 + 45) % 360, "Mistral")
        ]
        closest_direction = min(directions, key=lambda d: abs((wind_angle - d[0] + 360) % 360))
        wind_direction = closest_direction[1]

        # Mostrar la dirección y fuerza del viento
        font = pygame.font.SysFont(None, 36)
        text = font.render(f"Viento: {wind_direction} ({int(wind_strength * 10)} nudos)", True, WHITE)
        text_rect = text.get_rect()
        text_rect.topleft = (WIDTH - 300, 10)
        if text_rect.right > WIDTH:
            text_rect.right = WIDTH - 10
        if text_rect.bottom > HEIGHT:
            text_rect.bottom = HEIGHT - 10
        win.blit(text, text_rect.topleft)

        # Ajustar la flecha del viento si excede los límites de la pantalla
        arrow_length = 50 + wind_strength * 10  # Tamaño proporcional a la fuerza del viento
        wx = math.cos(math.radians(wind_angle)) * arrow_length
        wy = math.sin(math.radians(wind_angle)) * arrow_length

        arrow_end_x = 50 + wx
        arrow_end_y = 50 + wy

        if arrow_end_x > WIDTH:
            arrow_end_x = WIDTH - 10
        if arrow_end_x < 0:
            arrow_end_x = 10
        if arrow_end_y > HEIGHT:
            arrow_end_y = HEIGHT - 10
        if arrow_end_y < 0:
            arrow_end_y = 10

        pygame.draw.line(win, WHITE, (50, 50), (arrow_end_x, arrow_end_y), 3)

        # Dibujar las puntas de la flecha ajustadas
        arrow_head_size = 10
        angle_offset = math.radians(20)  # Ángulo de las puntas de la flecha
        left_x = arrow_end_x - math.cos(math.radians(wind_angle) - angle_offset) * arrow_head_size
        left_y = arrow_end_y - math.sin(math.radians(wind_angle) - angle_offset) * arrow_head_size
        right_x = arrow_end_x - math.cos(math.radians(wind_angle) + angle_offset) * arrow_head_size
        right_y = arrow_end_y - math.sin(math.radians(wind_angle) + angle_offset) * arrow_head_size

        pygame.draw.line(win, WHITE, (arrow_end_x, arrow_end_y), (left_x, left_y), 3)
        pygame.draw.line(win, WHITE, (arrow_end_x, arrow_end_y), (right_x, right_y), 3)
        #angle_text = font.render(f"Ángulo: {wind_angle}°", True, WHITE)
        #win.blit(angle_text, (WIDTH - 300, 50))
        # Mostrar el valor de effectiveness


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
            wind_strength = max(1, min(10, wind_strength + random.uniform(-1, 1)))
            wind_angle = (wind_angle + random.choice([-45, -30, -15, 0, 15, 30, 45])) % 360
            pygame.time.wait(200)

        draw_boat(boat_pos, boat_angle)
        draw_wind_arrow()

        pygame.display.update()
        clock.tick(30)

    pygame.quit()
