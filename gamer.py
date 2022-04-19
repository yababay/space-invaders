import pygame.key

from datetime import datetime

from player import Player
from bullet import Bullet
from settings import *


class Gamer(Player):

    def __init__(self, space, image=GAMER_DEFAULT_IMAGE, speed=GAMER_DEFAULT_SPEED):
        Player.__init__(self, space, image, speed)
        self.rect.center = ((GAME_WIDTH - PLAYER_DEFAULT_WIDTH) / 2, GAME_HEIGHT - PLAYER_DEFAULT_HEIGHT / 2)
        self.last_shot = datetime.now()

    def update(self, *args, **kwargs) -> None:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.left -= self.speed
            if self.rect.left <= 0:
                self.rect.left = 0
        if keys[pygame.K_RIGHT]:
            self.rect.right += self.speed
            if self.rect.right >= GAME_WIDTH:
                self.rect.right = GAME_WIDTH
        if keys[pygame.K_UP]:
            now = datetime.now()
            if now - self.last_shot < GAMER_BETWEEN_SHOTS:
                return
            self.last_shot = now
            bullet = Bullet(self.space, self)
            self.space.gamers.add(bullet)
