import circleshape
import pygame as p
import constants as c

class Shot(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, c.SHOT_RADIUS)

    def draw(self, screen):
        p.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt