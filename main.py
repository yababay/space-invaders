# Игра "Пришельцы из космоса"

from space import Space
from alien import Alien
from gamer import Gamer


def start_game():
    game = Space()
    alien = Alien(game)
    game.aliens.add(alien)
    gamer = Gamer(game)
    game.gamers.add(gamer)
    game.run()


if __name__ == '__main__':
    start_game()
