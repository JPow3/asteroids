import circleshape
import pygame as p
import constants as c
from shot import Shot

class Player(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, c.PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0

    def triangle(self):
        forward = p.Vector2(0, 1).rotate(self.rotation)
        right = p.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        p.draw.polygon(screen, "white", self.triangle(),  2)

    def rotate(self, dt):
        self.rotation += c.PLAYER_TURN_SPEED * dt

    def update(self, dt):
        self.shoot_timer -= dt
        keys = p.key.get_pressed()
        if keys[p.K_a]:
            self.rotate(-dt)
        if keys[p.K_d]:
            self.rotate(dt)
        if keys[p.K_w]:
            self.move(dt)
        if keys[p.K_s]:
            self.move(-dt)
        if keys[p.K_SPACE]:
            self.shoot()

    def move(self, dt):
        forward = p.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * c.PLAYER_SPEED * dt

    def shoot(self):
        if self.shoot_timer > 0:
            return
        self.shoot_timer = c.PLAYER_SHOOT_COOLDOWN
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = p.Vector2(0, 1).rotate(self.rotation) * c.PLAYER_SHOOT_SPEED
        
