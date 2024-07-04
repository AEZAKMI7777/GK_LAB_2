import pygame
import math

pygame.init()

window_width = 600
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Przekształcenie wielokąta")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Polygon:
    def __init__(self, num_sides, radius=150):
        self.num_sides = num_sides
        self.radius = radius
        self.center = (window_width // 2, window_height // 2)
        self.points = self.calculate_points()

    def calculate_points(self):
        angle_increment = (2 * math.pi) / self.num_sides
        points = [
            (
                self.center[0] + int(self.radius * math.cos(i * angle_increment)),
                self.center[1] + int(self.radius * math.sin(i * angle_increment))
            )
            for i in range(self.num_sides)
        ]
        return points

    def rotate(self, angle):
        angle_radians = math.radians(angle)
        rotated_points = [
            (
                self.center[0] + math.cos(angle_radians) * (x - self.center[0]) - math.sin(angle_radians) * (y - self.center[1]),
                self.center[1] + math.sin(angle_radians) * (x - self.center[0]) + math.cos(angle_radians) * (y - self.center[1])
            )
            for x, y in self.points
        ]
        self.points = rotated_points

    def skew(self, factor):
        skewed_points = [
            (x + factor * (y - self.center[1]), y)
            for x, y in self.points
        ]
        self.points = skewed_points

    def mirror(self, axis):
        if axis == "vertical":
            center_x = sum(x for x, _ in self.points) / len(self.points)
            mirrored_points = [(2 * center_x - x, y) for x, y in self.points]
        elif axis == "horizontal":
            center_y = sum(y for _, y in self.points) / len(self.points)
            mirrored_points = [(x, 2 * center_y - y) for x, y in self.points]
        self.points = mirrored_points

    def align_top(self):
        min_y = min(y for _, y in self.points)
        self.points = [(x, y - min_y) for x, y in self.points]

    def align_bottom(self):
        max_y = max(y for _, y in self.points)
        self.points = [(x, y - max_y + window_height) for x, y in self.points]

    def align_right(self):
        max_x = max(x for x, _ in self.points)
        self.points = [(x - max_x + window_width, y) for x, y in self.points]

    def widen(self, factor):
        center_y = sum(y for _, y in self.points) / len(self.points)
        self.points = [(x, center_y + factor * (y - center_y)) for x, y in self.points]

def transform_polygon(polygon, option):
    if option == 2:
        polygon.rotate(45)
    elif option == 3:
        polygon.rotate(180)
    elif option == 4:
        polygon.skew(1.5)
    elif option == 5:
        polygon.align_top()
    elif option == 6:
        polygon.skew(1.5)
        polygon.rotate(180)
    elif option == 7:
        polygon.rotate(180)
        polygon.mirror("vertical")
    elif option == 8:
        polygon.rotate(45)
        polygon.align_bottom()
        polygon.widen(1.5)
    elif option == 9:
        polygon.rotate(180)
        polygon.skew(1.5)
        polygon.align_right()

def main():
    running = True
    option = 1
    num_sides = 15  # Changed from 11 to 15
    polygon = Polygon(num_sides)
    font = pygame.font.Font(None, 14)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    option = 1
                elif event.key == pygame.K_2:
                    option = 2
                elif event.key == pygame.K_3:
                    option = 3
                elif event.key == pygame.K_4:
                    option = 4
                elif event.key == pygame.K_5:
                    option = 5
                elif event.key == pygame.K_6:
                    option = 6
                elif event.key == pygame.K_7:
                    option = 7
                elif event.key == pygame.K_8:
                    option = 8
                elif event.key == pygame.K_9:
                    option = 9

        window.fill(WHITE)
        polygon.points = polygon.calculate_points()  # Reset points to original before each transformation
        transform_polygon(polygon, option)
        pygame.draw.polygon(window, BLACK, polygon.points)

        mode_text = [
            "Wielokąt na środku okna",
            "Wielokąt przekręcony o 45 stopni",
            "Wielokąt odwrócony o 180 stopni",
            "Wielokąt pochylony w lewo",
            "Wielokąt przy górnej krawędzi okna",
            "Wielokąt odwrócony o 180 stopni i przekrzywiony w lewo",
            "Wielokąt odwrócony o 180 stopni i odwrócenie lustrzane",
            "Wielokąt odwrócony o 45 stopni oraz przy dolnej krawędzi",
            "Wielokąt odwrócony o 180 stopni pochylony w lewo oraz przy prawej krawędzi"
        ][option - 1]

        mode_text_surface = font.render("Tryb: " + mode_text, True, BLACK)
        window.blit(mode_text_surface, (10, 580))

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
