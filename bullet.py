from player import Player
from settings import *


class Bullet(Player):

    def __init__(self, space, gamer):
        Player.__init__(self, space, speed=BULLET_DEFAULT_SPEED, width=BULLET_DEFAULT_WIDTH,
                        height=BULLET_DEFAULT_HEIGHT, color=BULLET_DEFAULT_COLOR)
        self.rect.center = gamer.rect.center
        self.rect.bottom = gamer.rect.top
        self.gamer = gamer

    def update(self, *args, **kwargs) -> None:
        self.rect.y -= self.speed
        if self.rect.bottom < 0:
            self.space.gamers.remove(self)
        for alien in self.space.aliens:
            if self.rect.top <= alien.rect.bottom \
                    and self.rect.left > alien.rect.left \
                    and self.rect.right < alien.rect.right:
                self.space.aliens.remove(alien)
                self.space.gamers.remove(self)
                self.space.downed_count += 1
