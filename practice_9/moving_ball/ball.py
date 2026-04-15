import pygame

class Ball:
    def __init__(self, x, y, radius, screen_width, screen_height):
        self.x = x
        self.y = y
        self.radius = radius

        self.screen_width = screen_width
        self.screen_height = screen_height

        self.color = (255, 0, 0)

        self.base_speed = 3
        self.speed = self.base_speed
        self.max_speed = 15

    def update(self, keys):
        moving = False

        if keys[pygame.K_LEFT]:
            if self.x - self.radius > 0:
                self.x -= self.speed
            moving = True

        if keys[pygame.K_RIGHT]:
            if self.x + self.radius < self.screen_width:
                self.x += self.speed
            moving = True

        if keys[pygame.K_UP]:
            if self.y - self.radius > 0:
                self.y -= self.speed
            moving = True

        if keys[pygame.K_DOWN]:
            if self.y + self.radius < self.screen_height:
                self.y += self.speed
            moving = True

        # ускорение при удержании
        if moving:
            if self.speed < self.max_speed:
                self.speed += 0.3
        else:
            self.speed = self.base_speed

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)