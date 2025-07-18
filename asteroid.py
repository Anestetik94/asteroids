from circleshape import CircleShape
import pygame
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()  # Remove the current asteroid
        if self.radius <= ASTEROID_MIN_RADIUS:  # Minimum radius to split
            return
        else:
            angle = random.uniform(20, 50)
            asteroid1 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            asteroid2 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            asteroid1.velocity = self.velocity.rotate(angle)
            asteroid2.velocity = self.velocity.rotate(-angle)
            asteroid1.add(*Asteroid.containers)
            asteroid2.add(*Asteroid.containers)
