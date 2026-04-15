import pygame
import sys
from player import MusicPlayer

pygame.init()

WIDTH, HEIGHT = 700, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

font = pygame.font.SysFont("Arial", 32)
small = pygame.font.SysFont("Arial", 22)

player = MusicPlayer()

running = True

while running:
    screen.fill(WHITE)

    title = font.render("Music Player", True, BLACK)
    track = small.render("Track: " + player.get_name(), True, BLACK)

    controls = small.render(
        "P=Play  S=Stop  N=Next  B=Back  Q=Quit",
        True,
        BLACK
    )

    screen.blit(title, (50, 50))
    screen.blit(track, (50, 120))
    screen.blit(controls, (50, 250))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_p:
                player.play()

            elif event.key == pygame.K_s:
                player.stop()

            elif event.key == pygame.K_n:
                player.next()

            elif event.key == pygame.K_b:
                player.prev()

            elif event.key == pygame.K_q:
                running = False

pygame.quit()
sys.exit()