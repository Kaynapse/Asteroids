from circleshape import *
from constants import *
import pygame



class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
          

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (self.x, self.y), self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt