import pygame
from pygame.sprite import Sprite
from pygame import Surface
from settings import *


class Player(Sprite):  # Класс это "чертеж" для создания множества однотипных объектов.

    def __init__(self, space, image=None,
                 speed=PLAYER_DEFAULT_SPEED,
                 width=PLAYER_DEFAULT_WIDTH,
                 height=PLAYER_DEFAULT_HEIGHT,
                 color=PLAYER_DEFAULT_COLOR):  # Конструктор. Вызывается при создании нового объекта.
        Sprite.__init__(self)   # Наш класс расширяет класс Sprite (является наследником)
        if image:
            image = pygame.image.load(f'assets/bots/{image}.png')
            self.image = image
        else:
            image = Surface((width, height))
            image.fill(color)
            self.image = image
        self.rect = image.get_rect()
        self.space = space
        self.speed = speed

    def update(self, *args, **kwargs) -> None:
        pass
