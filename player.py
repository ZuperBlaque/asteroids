import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot

class Player(CircleShape):
    # Player class representing the spaceship
    def __init__(self, x, y, shots_group):
        # Call the parent constructor, and pass in PLAYER_RADIUS
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0  # in degrees
        self.shots_group = shots_group
        self.shoot_cooldown = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), width=2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            if self.shoot_cooldown <= 0:    # Check if the shoot cooldown is over
                self.shoot()
            elif self.shoot_cooldown > 0:   # Decrease the cooldown timer if it is still active
                self.shoot_cooldown -= dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        self.shots_group.add(shot)
        # Note: You might want to implement a cooldown mechanism to prevent shooting too rapidly.
        self.shoot_cooldown = 0.2
        
        