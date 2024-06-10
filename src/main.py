import pygame
import sys
import time
import random
import math
from personaje import Personaje
from enemigo import Enemigo
from objeto import Objeto
from escenario import Escenario

pygame.init()

# Configuración de pantalla
info = pygame.display.Info()
SCREEN_WIDTH, SCREEN_HEIGHT = info.current_w, info.current_h
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("UnHappy")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GOLD = (255, 215, 0)  # Definición del color oro

# Fuente
font = pygame.font.Font(None, 36)

# Cargar y redimensionar imágenes


def load_and_scale_image(path, width, height):
    image = pygame.image.load(path)
    return pygame.transform.scale(image, (width, height))


arquero_img = load_and_scale_image("arquero.png", 50, 50)
mago_img = load_and_scale_image("mago.png", 50, 50)
enemigo_img = load_and_scale_image("enemigo.png", 50, 50)
objeto_img = load_and_scale_image("objeto.png", 30, 30)

# Tamaño de los muros
WALL_WIDTH, WALL_HEIGHT = 50, 50


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def draw_variables(personaje, surface):
    draw_text(f'Vida: {personaje.puntos_de_vida}',
              font, WHITE, surface, 10, 10)
    draw_text(f'Ataque: {personaje.ataque}', font, WHITE, surface, 10, 40)
    draw_text(f'Defensa: {personaje.defensa}', font, WHITE, surface, 10, 70)
    draw_text(f'Nivel: {personaje.nivel}', font, WHITE, surface, 10, 100)
    draw_text(f'Experiencia: {personaje.experiencia}',
              font, WHITE, surface, 10, 130)


def main_menu():
    click = False
    while True:
        screen.fill(BLACK)
        draw_text('Menú Principal', font, WHITE, screen,
                  SCREEN_WIDTH // 2 - 90, SCREEN_HEIGHT // 2 - 200)
        mx, my = pygame.mouse.get_pos()

        button_play = pygame.Rect(
            SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 - 25, 110, 50)
        pygame.draw.rect(screen, GREEN if button_play.collidepoint(
            (mx, my)) else WHITE, button_play)
        draw_text('Jugar', font, BLACK, screen, SCREEN_WIDTH //
                  2 - 20, SCREEN_HEIGHT // 2 - 15)

        if button_play.collidepoint((mx, my)):
            if click:
                difficulty_selection()

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()


def difficulty_selection():
    click = False
    while True:
        screen.fill(BLACK)
        draw_text('Selecciona la Dificultad', font, WHITE, screen,
                  SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 200)
        mx, my = pygame.mouse.get_pos()

        button_easy = pygame.Rect(
            SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 - 75, 100, 50)
        button_medium = pygame.Rect(
            SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2, 100, 50)
        button_hard = pygame.Rect(
            SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 + 75, 100, 50)
        pygame.draw.rect(screen, GREEN if button_easy.collidepoint(
            (mx, my)) else WHITE, button_easy)
        pygame.draw.rect(screen, GREEN if button_medium.collidepoint(
            (mx, my)) else WHITE, button_medium)
        pygame.draw.rect(screen, GREEN if button_hard.collidepoint(
            (mx, my)) else WHITE, button_hard)
        draw_text('Fácil', font, BLACK, screen, SCREEN_WIDTH //
                  2 - 20, SCREEN_HEIGHT // 2 - 65)
        draw_text('Medio', font, BLACK, screen, SCREEN_WIDTH //
                  2 - 25, SCREEN_HEIGHT // 2 + 10)
        draw_text('Difícil', font, BLACK, screen, SCREEN_WIDTH //
                  2 - 20, SCREEN_HEIGHT // 2 + 85)

        if button_easy.collidepoint((mx, my)):
            if click:
                character_selection('easy')
        if button_medium.collidepoint((mx, my)):
            if click:
                character_selection('medium')
        if button_hard.collidepoint((mx, my)):
            if click:
                character_selection('hard')

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()


def character_selection(difficulty):
    click = False
    while True:
        screen.fill(BLACK)
        draw_text('Escoge tu clase:', font, WHITE, screen,
                  SCREEN_WIDTH // 2 - 90, SCREEN_HEIGHT // 2 - 200)
        mx, my = pygame.mouse.get_pos()

        button_arquero = pygame.Rect(
            SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2 - 25, 100, 50)
        button_mago = pygame.Rect(
            SCREEN_WIDTH // 2 + 100, SCREEN_HEIGHT // 2 - 25, 100, 50)
        pygame.draw.rect(screen, GREEN if button_arquero.collidepoint(
            (mx, my)) else WHITE, button_arquero)
        pygame.draw.rect(screen, GREEN if button_mago.collidepoint(
            (mx, my)) else WHITE, button_mago)
        draw_text('Arquero', font, BLACK, screen, SCREEN_WIDTH //
                  2 - 200, SCREEN_HEIGHT // 2 - 15)
        draw_text('Mago', font, BLACK, screen, SCREEN_WIDTH //
                  2 + 120, SCREEN_HEIGHT // 2 - 15)

        if button_arquero.collidepoint((mx, my)):
            if click:
                personaje = Personaje(7, 16, 13, 1, [['Arco', '', ''], ['', '', ''], [
                                      '', '', '']], SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
                personaje.imagen = arquero_img
                personaje.cadencia_disparo = 1  # 1 disparo por segundo
                game_loop(personaje, difficulty)
        if button_mago.collidepoint((mx, my)):
            if click:
                personaje = Personaje(10, 8, 7, 1, [['Bastón', '', ''], ['', '', ''], [
                                      '', '', '']], SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
                personaje.imagen = mago_img
                personaje.cadencia_disparo = 0.5  # 2 disparos por segundo
                game_loop(personaje, difficulty)

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()


def generar_enemigos(n, personaje, walls):
    enemigos = []
    for _ in range(n):
        while True:
            x = random.randint(0, SCREEN_WIDTH - enemigo_img.get_width())
            y = random.randint(0, SCREEN_HEIGHT - enemigo_img.get_height())
            new_enemy_rect = pygame.Rect(
                x, y, enemigo_img.get_width(), enemigo_img.get_height())
            if not any(new_enemy_rect.colliderect(pygame.Rect(wall['x'], wall['y'], WALL_WIDTH, WALL_HEIGHT)) for wall in walls):
                if not new_enemy_rect.colliderect(pygame.Rect(personaje.x - 100, personaje.y - 100, 200, 200)):
                    break
        enemigos.append({
            'x': x,
            'y': y,
            'dx': 0,
            'dy': 0,
            'vida': random.randint(1, 10),
            'ataque': random.randint(1, 5),
            'defensa': random.randint(1, 3)
        })
    return enemigos


def generar_objetos(n, personaje, walls):
    objetos = []
    for _ in range(n):
        while True:
            x = random.randint(0, SCREEN_WIDTH - objeto_img.get_width())
            y = random.randint(0, SCREEN_HEIGHT - objeto_img.get_height())
            new_object_rect = pygame.Rect(
                x, y, objeto_img.get_width(), objeto_img.get_height())
            if not any(new_object_rect.colliderect(pygame.Rect(wall['x'], wall['y'], WALL_WIDTH, WALL_HEIGHT)) for wall in walls):
                if not new_object_rect.colliderect(pygame.Rect(personaje.x - 100, personaje.y - 100, 200, 200)):
                    break
        objetos.append({'x': x, 'y': y, 'nombre': 'oro'})
    return objetos


def generar_muros(n):
    muros = []
    for _ in range(n):
        x = random.randint(0, SCREEN_WIDTH - WALL_WIDTH)
        y = random.randint(0, SCREEN_HEIGHT - WALL_HEIGHT)
        muros.append({'x': x, 'y': y})
    return muros


def game_loop(personaje, difficulty):
    running = True
    last_shot_time = 0
    inventario_abierto = False

    # Configuración de dificultad
    if difficulty == 'easy':
        num_enemigos = 5
        detection_distance = 200
        enemy_speed = 2.0
    elif difficulty == 'medium':
        num_enemigos = 10
        detection_distance = 300
        enemy_speed = 3.0
    elif difficulty == 'hard':
        num_enemigos = 15
        detection_distance = 400
        enemy_speed = 4.0

    escenario = Escenario(SCREEN_WIDTH, SCREEN_HEIGHT)
    muros = generar_muros(10)  # Generar 10 muros aleatorios
    # Genera enemigos según la dificultad
    enemigos = generar_enemigos(num_enemigos, personaje, muros)
    objetos = generar_objetos(3, personaje, muros)  # Genera 3 objetos
    reloj = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_i:
                    inventario_abierto = not inventario_abierto
                if event.key == pygame.K_ESCAPE:
                    running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            personaje.mover("arriba", SCREEN_WIDTH, SCREEN_HEIGHT, muros)
        if keys[pygame.K_s]:
            personaje.mover("abajo", SCREEN_WIDTH, SCREEN_HEIGHT, muros)
        if keys[pygame.K_a]:
            personaje.mover("izquierda", SCREEN_WIDTH, SCREEN_HEIGHT, muros)
        if keys[pygame.K_d]:
            personaje.mover("derecha", SCREEN_WIDTH, SCREEN_HEIGHT, muros)

        mx, my = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0]:  # Botón izquierdo del ratón
            current_time = time.time()
            if current_time - last_shot_time >= 1 / personaje.cadencia_disparo:
                personaje.disparar(mx, my)
                last_shot_time = current_time

        screen.fill(BLACK)

        # Dibujar muros
        for muro in muros:
            pygame.draw.rect(
                screen, WHITE, (muro['x'], muro['y'], WALL_WIDTH, WALL_HEIGHT))

        # Dibujar zonas de venta
        escenario.dibujar_zonas_venta(screen)

        # Dibujar áreas de exploración
        escenario.dibujar_areas_exploracion(screen)

        # Dibujar personaje
        screen.blit(personaje.imagen, (personaje.x, personaje.y))

        # Dibujar balas
        for bala in personaje.balas:
            bala['x'] += bala['dx']
            bala['y'] += bala['dy']
            pygame.draw.circle(
                screen, RED, (int(bala['x']), int(bala['y'])), 5)

        # Dibujar enemigos
        for enemigo in enemigos:
            screen.blit(enemigo_img, (enemigo['x'], enemigo['y']))

            # Colisión con el personaje
            if pygame.Rect(enemigo['x'], enemigo['y'], enemigo_img.get_width(), enemigo_img.get_height()).colliderect(pygame.Rect(personaje.x, personaje.y, personaje.imagen.get_width(), personaje.imagen.get_height())):
                personaje.recibir_ataque(enemigo['ataque'])
                if personaje.puntos_de_vida <= 0:
                    running = False

        # Eliminar enemigos al recibir disparos
        for bala in personaje.balas:
            bala['x'] += bala['dx']
            bala['y'] += bala['dy']
            pygame.draw.circle(
                screen, RED, (int(bala['x']), int(bala['y'])), 5)

            # Detectar colisión entre balas y enemigos
            for enemigo in enemigos[:]:
                if pygame.Rect(enemigo['x'], enemigo['y'], enemigo_img.get_width(), enemigo_img.get_height()).collidepoint((bala['x'], bala['y'])):
                    enemigo['vida'] -= personaje.ataque
                    personaje.balas.remove(bala)  # Eliminar bala
                    if enemigo['vida'] <= 0:
                        enemigos.remove(enemigo)  # Eliminar enemigo
                        personaje.aumentar_experiencia(10)
                    break

        # Hacer que los enemigos se dirijan hacia el personaje si están lo suficientemente cerca
        for enemigo in enemigos:
            dx = personaje.x - enemigo['x']
            dy = personaje.y - enemigo['y']
            dist = math.hypot(dx, dy)
            if dist < detection_distance:  # Distancia de detección del enemigo según la dificultad
                if dist != 0:
                    dx /= dist
                    dy /= dist
                # Velocidad de los enemigos según la dificultad
                enemigo['x'] += dx * enemy_speed
                enemigo['y'] += dy * enemy_speed

        # Dibujar objetos
        for objeto in objetos:
            screen.blit(objeto_img, (objeto['x'], objeto['y']))

            # Colisión con el personaje
            if pygame.Rect(objeto['x'], objeto['y'], objeto_img.get_width(), objeto_img.get_height()).colliderect(pygame.Rect(personaje.x, personaje.y, personaje.imagen.get_width(), personaje.imagen.get_height())):
                personaje.recolectar('oro')
                objetos.remove(objeto)

        # Explorar área
        escenario.explorar_area(personaje)

        # Verificar colisión con zonas de venta
        for zona in escenario.zonas_venta:
            if pygame.Rect(zona['x'], zona['y'], WALL_WIDTH, WALL_HEIGHT).colliderect(pygame.Rect(personaje.x, personaje.y, personaje.imagen.get_width(), personaje.imagen.get_height())):
                personaje.recolectar('arma')
                escenario.zonas_venta.remove(zona)

        # Dibujar variables
        draw_variables(personaje, screen)

        if inventario_abierto:
            draw_inventory(personaje.inventario)

        pygame.display.flip()

        # Check for victory
        if not enemigos:
            victory_menu()

    # Mostrar pantalla de reaparecer
    respawn_menu(personaje, difficulty)


def respawn_menu(personaje, difficulty):
    click = False
    while True:
        screen.fill(BLACK)
        draw_text('Has muerto', font, RED, screen,
                  SCREEN_WIDTH // 2 - 40, SCREEN_HEIGHT // 2 - 50)

        mx, my = pygame.mouse.get_pos()

        # Botón respawn
        button_respawn = pygame.Rect(
            SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 + 50, 125, 50)
        pygame.draw.rect(screen, GREEN if button_respawn.collidepoint(
            (mx, my)) else WHITE, button_respawn)
        draw_text('Reintentar', font, BLACK, screen,
                  SCREEN_WIDTH // 2 - 40, SCREEN_HEIGHT // 2 + 60)

        if button_respawn.collidepoint((mx, my)):
            if click:
                personaje.puntos_de_vida = 10  # Restaurar puntos de vida
                personaje.limpiar_inventario()  # Limpiar el inventario
                game_loop(personaje, difficulty)

        # Botón exit
        button_exit = pygame.Rect(
            SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 + 120, 125, 50)
        pygame.draw.rect(screen, GREEN if button_exit.collidepoint(
            (mx, my)) else WHITE, button_exit)
        draw_text('Salir', font, BLACK, screen, SCREEN_WIDTH //
                  2 - 20, SCREEN_HEIGHT // 2 + 130)

        if button_exit.collidepoint((mx, my)):  # Lógica del botón exit
            if click:
                pygame.quit()
                sys.exit()

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()


def victory_menu():
    click = False
    while True:
        screen.fill(BLACK)
        draw_text('¡Victoria!', font, GREEN, screen,
                  SCREEN_WIDTH // 2 - 40, SCREEN_HEIGHT // 2 - 50)
        mx, my = pygame.mouse.get_pos()

        # Botón exit
        button_exit = pygame.Rect(
            SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 + 120, 125, 50)
        pygame.draw.rect(screen, GREEN if button_exit.collidepoint(
            (mx, my)) else WHITE, button_exit)
        draw_text('Salir', font, BLACK, screen, SCREEN_WIDTH //
                  2 - 20, SCREEN_HEIGHT // 2 + 130)

        if button_exit.collidepoint((mx, my)):
            if click:
                pygame.quit()
                sys.exit()

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()


def draw_inventory(inventario):
    draw_text('Inventario:', font, WHITE, screen, SCREEN_WIDTH // 2 - 50, 50)

    for i in range(3):
        for j in range(3):
            x = SCREEN_WIDTH // 2 - 90 + j * 60
            y = SCREEN_HEIGHT // 2 - 90 + i * 60
            pygame.draw.rect(screen, WHITE, (x, y, 50, 50), 2)
            item = inventario[i][j]
            if item:
                draw_text(item, font, WHITE, screen, x + 15, y + 15)


if __name__ == "__main__":
    main_menu()
