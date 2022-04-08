import pygame
from player import Player, DEFAULT_SPEED, PLAYER_HEIGHT
from bullet import Bullet


class Gamer(Player):  # Класс это "чертеж" для создания множества однотипных объектов.
    def __init__(self, color, width, height, sprites, bot, speed=DEFAULT_SPEED):  # Конструктор. Вызывается при создании нового
        # объекта.
        Player.__init__(self, color, width, height, speed=speed)   # Наш класс расширяет класс Sprite
        # (является наследником)
        self.rect.center = (width / 2, height - PLAYER_HEIGHT / 2)
        self.sprites = sprites
        self.shot = 0
        self.bot = bot
#        self.game_over = 0

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
        if keys[pygame.K_UP]:
            if not self.shot:

                self.sprites.add(Bullet(self.width, self.height, self))
                self.shot = 1
