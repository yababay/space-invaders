import pygame
import random
from player import Player

BULLET_WIDTH = 4
BULLET_HEIGHT = 4
DEFAULT_SPEED = 15


class Bullet(Player):  # Класс это "чертеж" для создания множества однотипных объектов.

    def __init__(self, width, height, gamer, speed=DEFAULT_SPEED):  # Конструктор. Вызывается при создании нового
        # объекта.
        super().__init__("black", width, height,
                         speed=DEFAULT_SPEED,
                         player_height=BULLET_HEIGHT,
                         player_width=BULLET_WIDTH)  # Наш класс расширяет класс Sprite (является наследником)
        self.rect.x = gamer.rect.x + gamer.rect.width / 2
        self.rect.y = height - gamer.rect.height
        self.gamer = gamer

    def update(self, *args, **kwargs) -> None:
        if self.rect.top + 25 <= self.gamer.bot.rect.bottom and self.rect.left > self.gamer.bot.rect.left and \
                self.rect.right < self.gamer.bot.rect.right:  # Прямоугольники сталкнулись - цель поражена.
            self.gamer.shot = 2
            return
        self.rect.y -= self.speed
        if self.rect.top < 0:
#            self.gamer.game_over = True
            self.gamer.shot = 3
#            self.rect.bottom = self.height
