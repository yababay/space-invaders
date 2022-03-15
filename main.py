# This is a sample Python script.
import pygame
import random
import time

from gamer import Gamer
from bot import Bot

# Объявляем константы.
RED = (255, 0, 0)
GREEN = (0, 255, 0)

YELLOW = (255, 255, 0)
WIDTH = 400
HEIGHT = 400
DELAY = 100


def get_random_speed():
    return random.randrange(3, 10)


def start_game(title):  # Функция принимает 1 параметр - заголовок окна.
    pygame.init()  # Инициализируем фреймворк.
    screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Устанавливаем размер экрана.
    pygame.display.set_caption(title)  # Устанавливаем заголовок окна.
    all_sprites = pygame.sprite.Group()
    gamer = Gamer(RED, WIDTH, HEIGHT)  # Создаем нового игрока.
    all_sprites.add(gamer)
    bot = Bot(GREEN, WIDTH, HEIGHT)  # Создаем нового игрока.
    all_sprites.add(bot)

    running = True  # Программа работает пока эта переменная = тру.
    while running:  # Цикл бесконечный до 26 строки.
        pygame.time.delay(DELAY)  # Задержка на 1/10 сек.

        for event in pygame.event.get():  # Обработка событий.
            if event.type == pygame.QUIT:  # Если игру прекратили (закрыли окно и т.д.)
                running = False  # Цикл продолжаться не будет.
                print('Ending...')

        all_sprites.update()
        if gamer.rect.top <= bot.rect.bottom and (gamer.rect.left - 10 < bot.rect.left and gamer.rect.right
                                                  + 10 > bot.rect.right):
            running = False
        screen.fill(YELLOW)  # Закрашиваем экран красным.
        pygame.display.flip()  # Применить изменения.

#    font = all_sprites.draw(screen)

#    pygame.font.SysFont('couriernew', 40)  #
#    text = font.render(str('HELLO'), True, RED)
#   pygame.display.flip()  # Применить изменения.

#    screen.blit(text, (50, 50))
#   time.sleep(5)

    pygame.quit()  # После цикла.
    print("Game over")


if __name__ == '__main__':
    start_game('Простая игра')

