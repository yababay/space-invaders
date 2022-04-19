import time

import pygame

from datetime import datetime
from time import sleep
from pygame.sprite import Group
from pygame.font import Font
from alien import Alien
from settings import *

pygame.init()  # Инициализируем фреймворк.


class Space:

    aliens = Group()
    gamers = Group()
    font = Font('assets/PressStart2P-Regular.ttf', 30)

    def __init__(self):
        pygame.display.set_caption(GAME_TITLE)  # Устанавливаем заголовок окна.
        self.screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))  # Устанавливаем размер экрана.
        bg1 = pygame.image.load(BACKGROUND_IMAGE)
        bg2 = pygame.image.load(BACKGROUND_IMAGE)
        bg_width = bg1.get_width()
        bg_height = bg1.get_height()
        self.bg_x1 = 0 - (bg_width - GAME_WIDTH) / 2
        self.bg_y1 = 0
        self.bg_x2 = self.bg_x1
        self.bg_y2 = bg_height
        self.bg_height = bg_height
        self.background1 = bg1
        self.background2 = bg2
        self.last_alien_time = datetime.now()
        self.game_over = False
        self.downed_count = 0

    def run(self):
        while not self.game_over:  # Цикл бесконечный.
            pygame.time.delay(GAME_DELAY)  # Задержка.
            for event in pygame.event.get():  # Обработка событий.
                if event.type == pygame.QUIT:  # Если игру прекратили (закрыли окно и т.д.)
                    running = False  # Цикл продолжаться не будет.
            if self.downed_count >= GAME_MAX_DOWNED_COUNT:
                self.set_game_over(True)
            now = datetime.now()
            if now - self.last_alien_time > GAME_BETWEEN_ALIENS:
                alien = Alien(self)
                self.aliens.add(alien)
                self.last_alien_time = now
            self.aliens.update()
            self.gamers.update()
            self.draw_screen()
            self.aliens.draw(self.screen)
            self.gamers.draw(self.screen)
            pygame.display.flip()  # Применить изменения.

        pygame.quit()

    def set_game_over(self, is_success):
        self.game_over = True
        if is_success:
            for alien in self.aliens:
                self.aliens.remove(alien)
        for gamer in self.gamers:
            self.gamers.remove(gamer)
        color = GAME_SUCCESS_COLOR if is_success else GAME_FAILURE_COLOR
        text = GAME_SUCCESS_TEXT if is_success else GAME_FAILURE_TEXT
        self.draw_text(text, color)
        sleep(5)

    def draw_screen(self):
        self.screen.blit(self.background1, (self.bg_x1, self.bg_y1))
        self.screen.blit(self.background2, (self.bg_x2, self.bg_y2))
        self.bg_y1 -= BACKGROUND_SPEED
        self.bg_y2 -= BACKGROUND_SPEED
        if self.bg_y1 < 0 - self.bg_height:
            self.bg_y1 = self.bg_y2 + self.bg_height
        if self.bg_y2 < 0 - self.bg_height:
            self.bg_y2 = self.bg_y1 + self.bg_height

    def draw_text(self, text, color):
        text = self.font.render(text, True, color)
        self.screen.blit(text, (GAME_WIDTH / 2 - text.get_rect().width / 2,
                                GAME_HEIGHT / 2 - text.get_rect().height / 2))
        pygame.display.flip()
