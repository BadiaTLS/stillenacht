import random
import pygame
from stillenacht.canvas import Canvas

canvas = Canvas()


class Star:
    def __init__(self):
        self.__size = 1
        self.__color = [(255, 0, 0), (255, 255, 0)]
        self.__star_list = []

    def get_size(self):
        return self.__size

    def get_starlist(self):
        return self.__star_list

    def draw(self):
        for i in range(21):
            x = random.randrange(5, (canvas.width - 5))
            y = random.randrange(5, 100)
            self.__star_list.append([x, y])

    def shining(self, screen):

        for i in range(len(self.__star_list)):
            if random.randint(0, 1) == 0:
                pygame.draw.circle(screen, self.__color[0], self.__star_list[i], self.__size)
            else:
                pygame.draw.circle(screen, self.__color[1], self.__star_list[i], self.__size)
