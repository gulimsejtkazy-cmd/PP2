import pygame
import sys
from ball import Ball

pygame.init()

WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball")

WHITE = (255, 255, 255)

ball = Ball(WIDTH // 2, HEIGHT // 2, 25, WIDTH, HEIGHT)

clock = pygame.time.Clock()
running = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    ball.update(keys)

    screen.fill(WHITE)
    ball.draw(screen)

    pygame.display.update()

pygame.quit()
sys.exit()