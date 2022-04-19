import random

from player import Player
from settings import *


def get_random_x():
    return random.randint(0, GAME_WIDTH - PLAYER_DEFAULT_WIDTH)


def get_random_color():
    n = random.randint(0, len(ALIEN_IMAGES) - 1)
    return random.choice(ALIEN_IMAGES)


class Alien(Player):

    def __init__(self, space, speed=ALIEN_DEFAULT_SPEED):
        Player.__init__(self, space, get_random_color(), speed)
        self.rect.bottom = 0
        self.rect.x = get_random_x()

    def update(self, *args, **kwargs) -> None:
        self.rect.y += self.speed
        if self.rect.top >= GAME_HEIGHT:
            self.space.aliens.remove(self)
        if self.rect.bottom > GAME_HEIGHT - PLAYER_DEFAULT_HEIGHT:
            self.space.set_game_over(False)
