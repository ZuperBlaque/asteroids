import pygame
from circleshape import CircleShape
from constants import *

class Player(CircleShape):
    # Player class representing the spaceship
    def __init__(self, x, y):
        # Call the parent constructor, and pass in PLAYER_RADIUS
        super().__init__(x, y, PLAYER_RADIUS)
    rotation = 0  # in degrees0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), width=2)
