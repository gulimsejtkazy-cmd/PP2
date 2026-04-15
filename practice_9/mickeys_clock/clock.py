import pygame
import os
import datetime

pygame.init()

WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")
clock = pygame.time.Clock()

base = os.path.dirname(os.path.abspath(__file__))
img_path = os.path.join(base, "images")

def load_scale(name, size):
    img = pygame.image.load(os.path.join(img_path, name)).convert_alpha()
    return pygame.transform.smoothscale(img, size)

# 🔥 BIGGER SIZES
background_img = load_scale("background.png", (580, 580))   # clock
miki_img = load_scale("miki.png", (300, 300))               # 🐭 bigger Mickey
left_hand = load_scale("hand_left_centered.png", (60, 180)) # 🖐 bigger hand
right_hand = load_scale("hand_right_centered.png", (110, 110))

center = (WIDTH // 2, HEIGHT // 2)


def rotate(image, angle):
    rotated = pygame.transform.rotate(image, angle)
    rect = rotated.get_rect(center=center)
    return rotated, rect


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    now = datetime.datetime.now()

    seconds = now.second + now.microsecond / 1000000
    minutes = now.minute + seconds / 60

    # ⏱ angles
    second_angle = -6 * seconds + 90
    minute_angle = -6 * minutes + 90

    screen.fill((255, 255, 255))

    # 🕒 clock background
    bg_rect = background_img.get_rect(center=center)
    screen.blit(background_img, bg_rect)

    # 🐭 Mickey (bigger, inside clock)
    miki_rect = miki_img.get_rect(center=center)
    screen.blit(miki_img, miki_rect)

    # 🖐 hands (bigger)
    sec_img, sec_rect = rotate(left_hand, second_angle)
    min_img, min_rect = rotate(right_hand, minute_angle)

    screen.blit(sec_img, sec_rect)
    screen.blit(min_img, min_rect)

    pygame.draw.circle(screen, (0, 0, 0), center, 5)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()