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
HEIGHT = 800
DELAY = 100
pygame.init()  # Инициализируем фреймворк.
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Устанавливаем размер экрана.
font = pygame.font.SysFont('Arial', 40)


def get_random_speed():
    return random.randrange(3, 10)


def draw_text(text, color):
    text = font.render(text, True, color)
    screen.blit(text, (WIDTH / 2 - text.get_rect().width / 2, HEIGHT / 2 - text.get_rect().height / 2))


def start_game(title):  # Функция принимает 1 параметр - заголовок окна.
    pygame.display.set_caption(title)  # Устанавливаем заголовок окна.
    all_sprites = pygame.sprite.Group()
    bot = Bot(GREEN, WIDTH, HEIGHT)  # Создаем нового игрока.
    gamer = Gamer(RED, WIDTH, HEIGHT, all_sprites, bot)  # Создаем нового игрока.
    all_sprites.add(gamer)
    all_sprites.add(bot)

    running = True  # Программа работает пока эта переменная = тру.
    while running:  # Цикл бесконечный до 26 строки.
        pygame.time.delay(DELAY)  # Задержка на 1/10 сек.

        for event in pygame.event.get():  # Обработка событий.
            if event.type == pygame.QUIT:  # Если игру прекратили (закрыли окно и т.д.)
                running = False  # Цикл продолжаться не будет.
                print('Ending...')

        screen.fill(YELLOW)  # Закрашиваем экран красным.
        all_sprites.draw(screen)
        all_sprites.update()
        if gamer.rect.top + 5 <= bot.rect.bottom and (gamer.rect.left - 10 < bot.rect.left and gamer.rect.right
                                                      + 10 > bot.rect.right):
            running = False
            draw_text("You are winner.", "green")
        #            text = font.render("You are winner.", True, "black")
        #            screen.blit(text, (WIDTH / 2 - text.get_rect().width / 2, HEIGHT / 2 - text.get_rect().height / 2))
        elif bot.rect.bottom > HEIGHT:
            running = False
            draw_text("Game over.", "red")
        elif gamer.shot == 2:
            running = False
            draw_text("Target hit.", "blue")
        elif gamer.shot == 3:
            gamer.shot = 0
        #            running = False
        #            draw_text("You missed.", "black")

        #            text = font.render("Game over.", True, "black")
        #           screen.blit(text, (WIDTH / 2 - text.get_rect().width / 2, HEIGHT / 2 - text.get_rect().height / 2))
        pygame.display.flip()  # Применить изменения.

    time.sleep(5)

    pygame.quit()  # После цикла.
    print("Game over")


if __name__ == '__main__':
    start_game('Простая игра')
