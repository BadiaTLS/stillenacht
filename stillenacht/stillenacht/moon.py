import pygame
from stillenacht.canvas import Canvas

canvas = Canvas()


class Moon:
    def __init__(self):
        self.size = 40
        self.color = [128, 128, 128]
        self.moon_coordinat = []

    def get_size(self):
        return self.size

    def get_color(self):
        return self.color

    def draw(self):
        x = canvas.width - 50
        y = 50
        self.moon_coordinat = [x, y]

    def draw_moon(self, screen):
        pygame.draw.circle(screen, self.color, self.moon_coordinat, self.size)

    @staticmethod
    def getInstance():
        moon = Moon()
        for x in moon.moon_coordinat:
            if moon.moon_coordinat[x] > 0:
                raise TypeError("This is singleton")
            else:
                pass
