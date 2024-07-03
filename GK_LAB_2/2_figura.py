import pygame
import sys

pygame.init()

screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Square with Triangles")

square_vertices = [
    (100, 100),
    (300, 100),
    (300, 300),
    (100, 300)
]

green = (0, 255, 0)
white = (255, 255, 255)

def draw_triangle(vertices):
    pygame.draw.polygon(screen, green, vertices, 0)


def draw_square_with_triangles(vertices):
    draw_triangle([vertices[0], vertices[1], vertices[2]])
    draw_triangle([vertices[0], vertices[3], vertices[1]])


running = True
while running:
    screen.fill(white)

    draw_square_with_triangles(square_vertices)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
sys.exit()