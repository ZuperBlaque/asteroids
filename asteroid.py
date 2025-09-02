import pygame
import random
from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        center = (int(self.position.x), int(self.position.y))
        pygame.draw.circle(screen, "gray", center, int(self.radius), width=0)
        pygame.draw.circle(screen, (90, 0, 128), center, int(self.radius), width=7)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return []
        if self.radius > ASTEROID_MIN_RADIUS:
            # Create two smaller asteroids
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)  
            asteroid1.velocity = (self.velocity * 1.2).rotate(random.uniform(20, 50))
            asteroid2.velocity = (self.velocity * 1.2).rotate(random.uniform(-50, -20))
            return [asteroid1, asteroid2]
