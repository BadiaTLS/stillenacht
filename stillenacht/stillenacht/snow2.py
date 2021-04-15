import random
import pygame
from stillenacht.canvas import Canvas

canvas = Canvas()


class Snow:
    def __init__(self):
        self.__size = 2
        self.__color = [255, 255, 255]
        self.__x = random.randrange(0, canvas.width)
        self.__y = random.randrange(0, canvas.height)
        self.__snow_list = ((self.__x, self.__y))

    def get_size(self):
        return self.__size

    def get_color(self):
        return self.__color

    def falling(self, screen):
        for i in range((canvas.width // 2)):
            pygame.draw.circle(screen, self.__color, self.__snow_list[i], self.__size)
            self.__snow_list[i][1] += random.randrange(1, 3)
            if self.__snow_list[i][1] > canvas.height:
                y = random.randrange(-50, -5)
                self.__snow_list[i][1] = y
                x = random.randrange(canvas.width)
                self.__snow_list[i][0] = x
