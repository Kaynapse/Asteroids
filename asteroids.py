from circleshape import *
from constants import *
import pygame



class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
          

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (self.position.x, self.position.y), self.radius, width=2)
        print('drawing asteroid')

    def update(self, dt):
        self.position += self.velocity * dt
