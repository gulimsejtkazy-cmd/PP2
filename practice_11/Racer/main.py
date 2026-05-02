import pygame, sys
from pygame.locals import *
import random, time
import os
# папка проекта (чтобы правильно находить картинки и звуки)
BASE_DIR = os.path.dirname(__file__)

pygame.init()# запуск pygame

FPS = 60
FramePerSec = pygame.time.Clock()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
MONEY_SCORE = 0
next_speed = 10


moneta = pygame.image.load(os.path.join(BASE_DIR, "image", "money (1).png"))
gold_coin = pygame.image.load(os.path.join(BASE_DIR, "image", "golden_coin (1).png"))
silver_coin = pygame.image.load(os.path.join(BASE_DIR, "image", "silver_coin.png"))  # если нет (1)
bronze_coin = pygame.image.load(os.path.join(BASE_DIR, "image", "bronze_coin.png"))

background = pygame.image.load(os.path.join(BASE_DIR, "image", "AnimatedStreet (1).png"))
icon = pygame.image.load(os.path.join(BASE_DIR, "image", "icon.png"))

DISPLAYSURF = pygame.display.set_mode((400,600))
pygame.display.set_caption("Racer")
pygame.display.set_icon(icon)

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, (0,0,0))


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.types = [
            {"image": pygame.image.load(os.path.join(BASE_DIR, "image", "bronze_coin.png")), "value": 1},
            {"image": pygame.image.load(os.path.join(BASE_DIR, "image", "silver_coin.png")), "value": 2},
            {"image": pygame.image.load(os.path.join(BASE_DIR, "image", "golden_coin (1).png")), "value": 3}
        ]

        self.change_type()# выбираем случайную монету
        self.rect = self.image.get_rect()

        # появление сверху в случайной позиции
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)
    # смена типа монеты (бронза/серебро/золото)
    def change_type(self):
        t = random.choice(self.types)
        self.image = t["image"]
        self.value = t["value"]

    def move(self): # движение монеты вниз
        self.rect.move_ip(0, SPEED)
        # если монета ушла вниз — возвращаем её наверх
        if self.rect.top > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)
            self.change_type()


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join(BASE_DIR, "image", "Enemy (1).png"))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)

    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join(BASE_DIR, "image", "Player (1).png"))
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)# стартовая позиция

    def move(self): # управление игроком
        keys = pygame.key.get_pressed()

        if self.rect.left > 0 and keys[K_LEFT]:
            self.rect.move_ip(-5, 0)

        if self.rect.right < SCREEN_WIDTH and keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

# SPRITES
P1 = Player()
E1 = Enemy()
M1 = Coin()
# группы объектов (для удобного управления)
enemies = pygame.sprite.Group(E1)
money = pygame.sprite.Group(M1)
all_sprites = pygame.sprite.Group(P1, E1, M1)

# sound
bgsound = pygame.mixer.Sound(os.path.join(BASE_DIR, "sound", "background.wav"))
bgsound.play()

# game loop
while True:

    for event in pygame.event.get():
        # увеличение скорости игры по мере набора очков
        if MONEY_SCORE >= next_speed:
            SPEED += 3
            next_speed += 10

        if event.type == QUIT: # выход из игры
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(background, (0,0))

    for obj in all_sprites:
        DISPLAYSURF.blit(obj.image, obj.rect)
        obj.move()

    
    if pygame.sprite.spritecollideany(P1, enemies):
        bgsound.stop()
        pygame.mixer.Sound(os.path.join(BASE_DIR, "sound", "crash.wav")).play()
        time.sleep(0.5)

        waiting = True
        while waiting:
            DISPLAYSURF.fill((255,0,0))
            DISPLAYSURF.blit(game_over, (30,250))

            score = font_small.render(f"Score: {MONEY_SCORE}", True, (0,0,0))
            DISPLAYSURF.blit(score, (150,325))

            DISPLAYSURF.blit(font_small.render("R-restart", True, (0,0,0)), (150,500))
            DISPLAYSURF.blit(font_small.render("Q-quit", True, (0,0,0)), (150,525))

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == KEYDOWN:
                     # перезапуск игры
                    if event.key == K_r:
                        waiting = False
                        MONEY_SCORE = 0
                        SPEED = 5
                        E1.rect.top = 0
                        M1.rect.top = 0
                        bgsound.play()

                    if event.key == K_q:
                        pygame.quit()
                        sys.exit()

    # SCORE
    score_text = font_small.render(str(MONEY_SCORE), True, (255,255,0))
    DISPLAYSURF.blit(score_text, (10, 10))

    # COIN
    if pygame.sprite.spritecollideany(P1, money):
        pygame.mixer.Sound(os.path.join(BASE_DIR, "sound", "lost_money.wav")).play()
        MONEY_SCORE += M1.value # добавляем очки
        M1.rect.top = 0
        M1.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)
        M1.change_type()

    pygame.display.update()
    FramePerSec.tick(FPS)