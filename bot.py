import pygame
import random
from player import Player, DEFAULT_SPEED


class Bot(Player):  # Класс это "чертеж" для создания множества однотипных объектов.

    def __init__(self, color, width, height, speed=DEFAULT_SPEED):  # Конструктор. Вызывается при создании нового объекта.
        super().__init__(color, width, height, speed=DEFAULT_SPEED)   # Наш класс расширяет класс Sprite (является наследником)
        self.rect.x = self.get_random_x()

    def update(self, *args, **kwargs) -> None:
        self.rect.y += self.speed
        if self.rect.top > self.height:
            self.rect.bottom = 0
            self.rect.x = self.get_random_x()

    def get_random_x(self):
        return random.randint(0, self.width)
