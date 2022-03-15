import pygame
from player import Player, DEFAULT_SPEED, PLAYER_HEIGHT


class Gamer(Player):  # Класс это "чертеж" для создания множества однотипных объектов.
    def __init__(self, color, width, height, speed=DEFAULT_SPEED):  # Конструктор. Вызывается при создании нового объекта.
        Player.__init__(self, color, width, height, speed=speed)   # Наш класс расширяет класс Sprite (является наследником)
        self.rect.center = (width / 2, height - PLAYER_HEIGHT / 2)

    def update(self, *args, **kwargs) -> None:  # Заглушка, будет риолизовано в бот и геймер.
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            if self.rect.left <= 0:
                self.rect.left = 0
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            if self.rect.right >= self.width:
                self.rect.right = self.width
