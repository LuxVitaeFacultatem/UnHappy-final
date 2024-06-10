import random
import pygame

# Añadir las dimensiones de los muros si no están definidas
WALL_WIDTH, WALL_HEIGHT = 50, 50


class Escenario:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.zonas_venta = self.generar_zonas_venta(
            3)  # Generar 3 zonas de venta aleatorias
        self.areas = self.generar_areas_exploracion(
            5)  # Generar 5 áreas de exploración

    def generar_zonas_venta(self, n):
        zonas = []
        for _ in range(n):
            x = random.randint(0, self.width - WALL_WIDTH)
            y = random.randint(0, self.height - WALL_HEIGHT)
            zonas.append({'x': x, 'y': y})
        return zonas

    def generar_areas_exploracion(self, n):
        areas = []
        for _ in range(n):
            x = random.randint(0, self.width - WALL_WIDTH)
            y = random.randint(0, self.height - WALL_HEIGHT)
            areas.append({'x': x, 'y': y, 'descubierto': False})
        return areas

    def dibujar_zonas_venta(self, screen):
        for zona in self.zonas_venta:
            pygame.draw.rect(screen, (255, 215, 0),
                             (zona['x'], zona['y'], WALL_WIDTH, WALL_HEIGHT))

    def dibujar_areas_exploracion(self, screen):
        for area in self.areas:
            color = (0, 255, 0) if area['descubierto'] else (255, 255, 255)
            pygame.draw.rect(
                screen, color, (area['x'], area['y'], WALL_WIDTH, WALL_HEIGHT))

    def explorar_area(self, personaje):
        for area in self.areas:
            if pygame.Rect(area['x'], area['y'], WALL_WIDTH, WALL_HEIGHT).colliderect(pygame.Rect(personaje.x, personaje.y, 50, 50)):
                area['descubierto'] = True
