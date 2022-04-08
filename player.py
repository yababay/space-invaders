import pygame

PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
DEFAULT_SPEED = 5


class Player(pygame.sprite.Sprite):  # Класс это "чертеж" для создания множества однотипных объектов.

    def __init__(self, color, width, height, speed=DEFAULT_SPEED, player_width=PLAYER_WIDTH,
                 player_height=PLAYER_HEIGHT):  # Конструктор. Вызывается при создании нового объекта.
        pygame.sprite.Sprite.__init__(self)   # Наш класс расширяет класс Sprite (является наследником)
        self.image = pygame.Surface((player_width, player_height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.width = width
        self.height = height
        self.speed = speed

    def update(self, *args, **kwargs) -> None:
        pass
